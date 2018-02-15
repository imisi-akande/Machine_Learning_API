from rest_framework import serializers
from . import models


class DetectorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'headline', 'body', 'pub_date', 'fakeness',)
        model = models.News
        