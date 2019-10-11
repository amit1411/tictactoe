from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import game_detail, make_move, AllGamesList, delete_game


urlpatterns = [
    url(r'detail/(?P<id>\d+)/$',
        game_detail,
        name="gameplay_detail"),
    url(r'make_move/(?P<id>\d+)/',
        make_move,
        name="gameplay_make_move"),
    url(r'all$', AllGamesList.as_view()),
    url(r'delete_game/(?P<id>\d+)/$', delete_game, name="gameplay_delete_game")
]
