from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"title": "Este campo não pode estar vazio."})
        if not data.get('description'):
            raise serializers.ValidationError({"description": "Este campo não pode estar vazio."})
        return data