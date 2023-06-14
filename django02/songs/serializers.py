from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['name', 'duration', 'band']


class SongReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='song_review.id')

    class Meta:
        model = models.SongReviewComment
        fields = ['id', 'user', 'user_id', 'review', 'content']


class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = SongReviewCommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    def get_comment_count(self, obj):
        return models.SongReviewComment.objects.filter(song_review=obj).count()

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'user_id','song', 'content', 'score', 'comment_count','comments']