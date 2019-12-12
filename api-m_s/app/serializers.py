from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import User, Task

class UserSerializer(ModelSerializer):
    task = StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'task')
        extra_kwargs = {
            'id': {'read_only': True},
            'task': {'read_only': True}
        }

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'state', 'user_id')