from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Program, Day, Exercise, Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'date', 'rep', 'comment']


class WorkoutCreateSerializer(serializers.ModelSerializer):
    exercise_id = serializers.IntegerField(write_only=True)
    date = serializers.DateField(required=False)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'rep', 'comment', 'exercise_id']


class WorkoutBulkSerializer(serializers.Serializer):
    workouts = WorkoutCreateSerializer(many=True)

    def create(self, validated_data):
        workouts_data = validated_data.get('workouts')
        workouts_lst = []
        for workout_data in workouts_data:
            exercise_id = workout_data.pop('exercise_id')
            workouts_lst.append(Workout(exercise_id=exercise_id, **workout_data))
        Workout.objects.bulk_create(workouts_lst)
        return WorkoutSerializer(workouts_lst, many=True).data


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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        """Создание пользователя"""
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])
        return user
