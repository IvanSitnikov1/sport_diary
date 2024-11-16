from rest_framework import generics, status
from rest_framework.response import Response

from .models import Program, Workout
from .serializers import ProgramSerializer, WorkoutSerializer, \
    WorkoutBulkSerializer


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
