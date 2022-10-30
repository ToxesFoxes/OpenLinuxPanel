from rest_framework import serializers
from .models import SystemStat
class SystemStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStat
        fields = ['id', 'name', 'order', 'active', 'user']