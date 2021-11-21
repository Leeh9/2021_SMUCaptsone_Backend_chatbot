from rest_framework import serializers
from .models import Psycology


class PsycologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Psycology
        fields = ['textinput','textoutput']

