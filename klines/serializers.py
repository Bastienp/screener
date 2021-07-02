from rest_framework import serializers

class KlineSerializer(serializers.Serializer):
   klines = serializers.ListField()