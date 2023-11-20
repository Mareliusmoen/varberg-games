from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.models import Q, F, Count

from postman.models import Message


class Command(BaseCommand):
    help = (
        "Can be run as a cron job or directly to "
        "check-up data consistency in the database."
    )
    # no more NoArgsCommand and handle_noargs with Dj >= 1.8

    def handle(self, *args, **options):
        """
        Handle the command by checking messages and conversations for errors.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            None. Outputs the number of inconsistencies found or
            "All is correct" if no inconsistencies are found.
        """
        verbose = int(options.get('verbosity'))
        if verbose >= 1:
            self.stdout.write(datetime.now().strftime(
                "%H:%M:%S ") + "Checking messages + conversations for errors")
        checks = [
            ("Sender and Recipient cannot be both undefined.",
                Q(sender__isnull=True, recipient__isnull=True)),
            ("Visitor's email is in excess.", Q(
                sender__isnull=False, recipient__isnull=False) & ~Q(email='')),
            (
                "Visitor's email is missing.",
                (
                    (Q(sender__isnull=True) | Q(recipient__isnull=True))
                    & Q(email='')
                )
            ),
            ("Reading date must be later than sending date.",
                Q(read_at__lt=F('sent_at'))),
            ("Deletion date by sender must be later than sending date.",
                Q(sender_deleted_at__lt=F('sent_at'))),
            ("Deletion date by recipient must be later than sending date.",
                Q(recipient_deleted_at__lt=F('sent_at'))),
            ("Response date must be later than sending date.",
                Q(replied_at__lt=F('sent_at'))),
            ("The message cannot be replied without having been read.",
                Q(replied_at__isnull=False, read_at__isnull=True)),
            ("Response date must be later than reading date.",
                Q(replied_at__lt=F('read_at'))),
            # because of the delay due to the moderation, no constraint between
            #  replied_at and recipient_deleted_at
            (
                "Response date cannot be set without at least one reply.",
                Q(replied_at__isnull=False),
                {'cnt': Count('next_messages')},
                Q(cnt=0)
            ),
            # cnt should filter to allow only accepted replies, but do not
            # know how to specify it
            ("The message cannot be replied without being in a conversation.",
                Q(replied_at__isnull=False, thread__isnull=True)),
            ("The message cannot be a reply without being in a conversation.",
                Q(parent__isnull=False, thread__isnull=True)),
            (
                "The reply and its parent are not in a conversation in common",
                (
                    Q(parent__isnull=False, thread__isnull=False)
                    & (
                        Q(parent__thread__isnull=True)
                        | ~Q(parent__thread=F('thread'))
                    )
                )
            ),
        ]
        count = 0
        for c in checks:
            msgs = Message.objects.filter(c[1])
            if len(c) >= 4:
                msgs = msgs.annotate(
                    **c[2]).filter(c[3]).order_by('-sent_at', '-id')
            if msgs:
                count += len(msgs)
                self.report_errors(c[0], msgs)
        if verbose >= 1:
            self.stdout.write(
                datetime.now().strftime("%H:%M:%S ") + (
                    (
                        "Number of inconsistencies found: {0}. "
                        "See details on the error stream."
                    ).format(count)
                    if count
                    else "All is correct."
                )
            )


def report_errors(self, reason, msgs):
    """
    Report errors and display messages.

    Args:
        self (object): The current instance of the class.
        reason (str): The reason for the error.
        msgs (list): A list of messages to be displayed.

    Returns:
        None

    Description:
        This function takes in a reason and a list of messages and reports
        the errors by writing the reason to the standard error output.
        It then displays the messages in a tabular format.

        The function first writes the reason to the standard error output
        using the `write` method of the `stderr` object.

        It then formats and writes the header row of the table using the
        `write` method of the `stderr` object. 
        The header row contains the following columns: "Id", "From", "To",
        "Email", "Parent", "Thread", "Sent", "Read", "Replied".

        Next, it iterates over each message in the `msgs` list and formats
        and writes each message in a row of 
        the table using the `write` method of the `stderr` object.
        Each row contains the following columns: 
        "Id", "From", "To", "Email", "Parent", "Thread",
        "Sent", "Read", "Replied".

        The function does not return any value.

    """
    self.stderr.write(reason)
    self.stderr.write(
        "{0:6} {1:5} {2:5} {3:10} {4:6} {5:6} {6:16} {7:16} {8:16}".format(
            "Id", "From", "To", "Email", "Parent", "Thread",
            "Sent", "Read", "Replied"
        )
    )
    for msg in msgs:
        self.stderr.write(
            "{0.pk:6} {0.sender_id!s:5} {0.recipient_id!s:5} {0.email:10.10}"
            " {0.parent_id!s:6} {0.thread_id!s:6} {0.sent_at!s:16.16}"
            " {0.read_at!s:16.16} {0.replied_at!s:16.16}".format(msg)
        )
