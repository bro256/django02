from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongReviewList.as_view()),
    path('<int:pk>/', views.SongReviewDetail.as_view()),
]