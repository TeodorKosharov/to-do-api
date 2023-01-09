from to_do_app.core.models import Task
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if data['priority'] <= 0:
            raise ValidationError({'priority': 'Priority must be a positive integer and greater than 0!'})
        return data
