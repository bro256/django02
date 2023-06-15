from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongList.as_view()),
    path('song-reviews/', views.SongReviewList.as_view()),
    path('song-reviews/<int:pk>/', views.SongReviewDetail.as_view()),
    path('song-reviews/<int:review_pk>/comments/', views.SongReviewCommentList.as_view()),
    path('comment/<int:pk>/', views.SongReviewCommentDetail.as_view()),
    # path('<int:pk>/like/', views.SongReviewLikeCreateDestroy.as_view()),
]