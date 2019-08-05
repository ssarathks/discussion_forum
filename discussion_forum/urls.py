from django.conf.urls import url
from discussion_forum import views
app_name='discussion_forum'

urlpatterns=[
    url(r'^$',views.ThreadListView.as_view(),name='discussion_homepage'),
    url(r'^create_thread/$',views.create_thread,name='create_thread'),
    url(r'^thread/(?P<pk>\d+)/$',views.ThreadDetailView.as_view(),name='thread_detail'),
    url(r'^thread/(?P<pk>\d+)/create_comment/$',views.create_comment,name='create_comment'),
]
