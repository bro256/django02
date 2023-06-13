from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'song', 'content', 'score']
