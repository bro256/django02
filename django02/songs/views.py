from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from . import models, serializers


class SongList(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer

class SongReviewList(generics.ListAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SongReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        review = models.SongReview.objects.filter(
            pk=kwargs['pk'],
            user=request.user
        )
        if review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to do this'))
        
    def delete(self, request, *args, **kwargs):
        review = models.SongReview.objects.filter(
            pk=kwargs['pk'],
            user=request.user
        )
        if review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to do this.'))


class SongReviewCommentList(generics.ListCreateAPIView):
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        review = models.SongReview.objects.get(pk=self.kwargs['review_pk'])
        serializer.save(user=self.request.user, review=review)

    def get_queryset(self):
        review = models.SongReview.objects.get(pk=self.kwargs['review_pk'])
        return models.SongReview.objects.filter(review=review)


class SongReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        try:
            comment = models.SongReview.objects.get(pk=kwargs['pk'], user=request.user)
        except Exception as e:
            raise ValidationError(_('You cannot update this.'))
        else:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            comment = models.SongReview.objects.get(pk=kwargs['pk'], user=request.user)
        except Exception as e:
            raise ValidationError(_('You cannot delete this.'))
        else:
            return self.delete(request, *args, **kwargs)

