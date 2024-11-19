from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Program, Workout
from .serializers import ProgramSerializer, WorkoutSerializer, \
    WorkoutBulkSerializer, UserSerializer


class ProgramCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class WorkoutCreate(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutBulkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        workouts = serializer.save()
        return Response(workouts, status=status.HTTP_201_CREATED)


class WorkoutDestroy(generics.DestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    """Создаются точки создания, получения и изменения пользователя"""
    queryset = User.objects.all()
    http_method_names = ['post', 'put', 'get']
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
