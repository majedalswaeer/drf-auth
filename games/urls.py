from django.urls import path,include
from .views import GamesList,GamesDetail

urlpatterns=[
    path('',GamesList.as_view(),name='game_list'),
    path('<int:pk>/',GamesDetail.as_view(),name='game_detail'),

]