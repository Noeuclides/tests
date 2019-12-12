from django.conf.urls import url

from app.views import UserCreateView, UserDetailView, TaskCreateView, TaskDetailView

urlpatterns = [
    url(r'^user/$', UserCreateView.as_view(), name='user'),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetailView.as_view(), name='detail'),
    url(r'^user_task/$', TaskCreateView.as_view(), name='task'),
    url(r'^user_task/(?P<pk>[0-9]+)$', TaskDetailView.as_view(), name='task_detail'),
    url(r'^(?P<fk>[0-9]+)/user_task/$', TaskDetailView.as_view(), name='task_detail'),
]