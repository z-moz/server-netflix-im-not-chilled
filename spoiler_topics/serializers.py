from rest_framework import serializers
from .models import SpoilerTopic

class SpoilerTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpoilerTopic
        fields = ('id', 'topic_title','netflix_id','yes_vote','no_vote')