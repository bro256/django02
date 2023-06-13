from rest_framework import generics, permissions
from . import models, serializers


# class SongList(generics.ListAPIView):
#     queryset = models.Song.objects.all()
#     serializer_class = serializers.SongSerializer

class SongReviewList(generics.ListAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)