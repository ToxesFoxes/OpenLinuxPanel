from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import SystemStat
from .serializers import SystemStatsSerializer

class SystemStatsView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        stats = SystemStat.objects.filter(user = request.user.id)
        stats = stats.order_by('order')
        if not stats:
            stats = SystemStat.objects.create(name = 'cpu', order = 1, user = request.user)
            stats = SystemStat.objects.create(name = 'memory', order = 2, user = request.user)
            stats = SystemStat.objects.create(name = 'disk', order = 3, user = request.user)
            stats = SystemStat.objects.filter(user = request.user.id)
        serializer = SystemStatsSerializer(stats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        for stat in request.data:
            SystemStat.objects.filter(user = request.user.id, name = stat['name']).update(order = stat['order'], active = stat['active'])
        stats = SystemStat.objects.filter(user = request.user.id)
        serializer = SystemStatsSerializer(stats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)