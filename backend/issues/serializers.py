from .models import Issue
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from datetime import datetime

class DateSerializerField(ReadOnlyField):

    def to_representation(self, value):
        return value.strftime("%d/%m/%Y - %H:%M") if value else None

class IssueSerializer(ModelSerializer):

    last_updated = DateSerializerField()
     
    class Meta:

        model = Issue
        fields = '__all__'
