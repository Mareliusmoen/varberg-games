from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db.models import Max, Count, F, Q
from django.utils.timezone import now

from postman.models import Message

ARGUMENT_ARGS = ('-d', '--days')
ARGUMENT_KWARGS = {'default': 30}


class Command(BaseCommand):
    help = """Can be run as a cron job or directly to clean out old data
    from the database:
    Messages or conversations marked as deleted by both sender and recipient,
    more than a minimal number of days ago."""

    def add_arguments(self, parser):
        """
        Adds the necessary arguments to the argument parser.

        :param parser: The argument parser object to which the arguments
        will be added.
        :type parser: ArgumentParser

        :return: None
        """
        parser.add_argument(*ARGUMENT_ARGS, type=int,
                            help=(
                                'The minimal number of days a message is kept'
                                'marked as deleted, '
                                'before to be considered for real deletion '
                                '[default: %(default)s]'
                            ),
                            **ARGUMENT_KWARGS)

    # no more NoArgsCommand and handle_noargs with Dj >= 1.8
    def handle(self, *args, **options):
        """
        Deletes messages and conversations marked as deleted before a
        specified date.

        Parameters:
            *args: Variable length argument list.
            **options: Keyword arguments.

        Returns:
            None
        """
        verbose = int(options.get('verbosity'))
        days = options.get('days')
        date = now() - timedelta(days=days)
        if verbose >= 1:
            self.stdout.write(
                "Erase messages and conversations marked as deleted before {0}"
                .format(date)
            )
    # for a conversation to be candidat
        tpks = Message.objects.filter(
            thread__isnull=False).values('thread').annotate(
            cnt=Count('pk'),
            s_max=Max('sender_deleted_at'),
            s_cnt=Count('sender_deleted_at'),
            r_max=Max('recipient_deleted_at'),
            r_cnt=Count('recipient_deleted_at')
        ).order_by().filter(
            s_cnt=F('cnt'), r_cnt=F('cnt'), s_max__lte=date, r_max__lte=date
        ).values_list('thread', flat=True)

        Message.objects.filter(
            Q(thread__in=tpks) |
            Q(
                thread__isnull=True, sender_deleted_at__lte=date,
                recipient_deleted_at__lte=date
            )
        ).delete()
