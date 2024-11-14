from rest_framework import generics
from .models import Program
from .serializers import ProgramSerializer


class ProgramCreateView(generics.CreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
