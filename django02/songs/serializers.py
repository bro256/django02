from rest_framework import serializers
from . import models


# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Song
#         fields = ['name', 'duration', 'band']

# class SongReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.SongReview
#         fields = ['id', 'user', 'song', 'content', 'score']

class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'user_id', 'song', 'content', 'score']