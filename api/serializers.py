from rest_framework import serializers

from .models import Program, Day, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'rep']

class DaySerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Day
        fields = ['comment', 'date', 'exercises']


class ProgramSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)

    class Meta:
        model = Program
        fields = ['name', 'description', 'days']

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        user = self.context['request'].user
        program = Program.objects.create(user=user, **validated_data)
        for day_data in days_data:
            exercises_data = day_data.pop('exercises')
            day = Day.objects.create(program=program, **day_data)
            for exercise_data in exercises_data:
                Exercise.objects.create(day=day, **exercise_data)

        return program
