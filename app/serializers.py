from rest_framework import serializers


class APIInputCheckup(serializers.Serializer):
    content = serializers.CharField(allow_null=False, allow_blank=False)
    title = serializers.CharField(allow_null=False, allow_blank=False)