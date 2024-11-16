from rest_framework import generics
from .models import Program, Workout
from .serializers import ProgramSerializer, WorkoutSerializer


class ProgramCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class WorkoutCreate(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
