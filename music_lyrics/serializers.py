# music_lyrics/serializers.py
from rest_framework import serializers
from .models import Lyrics

class LyricsSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the Lyrics model.
    Converts Lyrics model instances into JSON format and validates input data.
    """
    class Meta:
        model = Lyrics
        fields = ['id', 'title', 'artist', 'lyrics']