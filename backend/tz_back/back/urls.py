from django.conf.urls import url
from .views import UserStatisticsView, UsersView


app_name = "back"

urlpatterns = [
    url(r'^users/$', UsersView.as_view()),
    url(r'^users/(?P<id>\d+)/$', UserStatisticsView.as_view()),
]

