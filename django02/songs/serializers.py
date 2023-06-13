from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['name', 'duration', 'band']
