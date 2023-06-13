from rest_framework import generics
from . import models, serializers


class PostList(generics.ListAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.PostSerializer
