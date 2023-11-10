from django.urls import include, re_path, path
from .views import autocomplete_recipients
from .views import (
    InboxView, SentView, ArchivesView, TrashView,
    WriteView, ReplyView, MessageView, ConversationView,
    ArchiveView, DeleteView, UndeleteView, MarkReadView, MarkUnreadView,
    IndexView
)
from . import api_urls

app_name = 'postman'
urlpatterns = [
    re_path(r'^inbox/(?:(?P<option>m)/)?$', InboxView.as_view(), name='inbox'),
    re_path(r'^sent/(?:(?P<option>m)/)?$', SentView.as_view(), name='sent'),
    re_path(r'^archives/(?:(?P<option>m)/)?$', ArchivesView.as_view(), name='archives'),
    re_path(r'^trash/(?:(?P<option>m)/)?$', TrashView.as_view(), name='trash'),
    re_path(r'^write/(?:(?P<recipients>[^/#]+)/)?$', WriteView.as_view(), name='write'),
    re_path(r'^reply/(?P<message_id>[\d]+)/$', ReplyView.as_view(), name='reply'),
    re_path(r'^view/(?P<message_id>[\d]+)/$', MessageView.as_view(), name='view'),
    re_path(r'^view/t/(?P<thread_id>[\d]+)/$', ConversationView.as_view(), name='view_conversation'),
    re_path(r'^archive/$', ArchiveView.as_view(), name='archive'),
    re_path(r'^delete/$', DeleteView.as_view(), name='delete'),
    re_path(r'^undelete/$', UndeleteView.as_view(), name='undelete'),
    re_path(r'^mark-read/$', MarkReadView.as_view(), name='mark-read'),
    re_path(r'^mark-unread/$', MarkUnreadView.as_view(), name='mark-unread'),
    re_path(r'^$', IndexView.as_view()),

    re_path(r'^api/', include(api_urls)),
    re_path(r'^write/$', WriteView.as_view(autocomplete_channels=(None,'anonymous_ac')), name='write'),
    re_path(r'^reply/$', ReplyView.as_view(autocomplete_channel='reply_ac'), name='reply'),
    path('autocomplete_recipients/', autocomplete_recipients, name='autocomplete_recipients'),
]