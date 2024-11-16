from rest_framework import serializers

from .models import Program, Day, Exercise, Workout


class WorkoutSerializer(serializers.ModelSerializer):
    exercise_id = serializers.IntegerField(write_only=True)
    date = serializers.DateField(required=False)
    class Meta:
        model = Workout
        fields = ['id', 'date', 'rep', 'comment', 'exercise_id']

    def create(self, validated_data):
        exercise_id = validated_data.pop('exercise_id')
        exercise = Exercise.objects.get(pk=exercise_id)
        workout = Workout.objects.create(exercise=exercise, **validated_data)
        return workout


class ExerciseSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True)

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'workouts']

class DaySerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Day
        fields = ['id', 'exercises']


class ProgramSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)

    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'days']

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        user = self.context['request'].user
        program = Program.objects.create(user=user, **validated_data)
        for day_data in days_data:
            exercises_data = day_data.pop('exercises')
            day = Day.objects.create(program=program)
            for exercise_data in exercises_data:
                workouts_data = exercise_data.pop('workouts')
                exercise = Exercise.objects.create(day=day, **exercise_data)
                for workout_data in workouts_data:
                    Workout.objects.create(exercise=exercise, **workout_data)

        return program
