from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

from api.models import Program, Exercise, Day, Workout
from api.serializers import ProgramSerializer


class ProgramWorkoutTest(APITestCase):
    def setUp(self):
        user_test = User.objects.create_user(
            username='user_test', password='user_test'
        )
        user_test.save()
        self.client.force_authenticate(user=user_test)

        self.program = Program.objects.create(
            name='program test',
            description='description test',
            user=user_test,
        )
        self.day = Day.objects.create(program=self.program)
        self.exercise = Exercise.objects.create(
            name='exercise test', day=self.day
        )

        self.create_program_data = {
            "name": "program",
            "description": "description",
            "days": [
                {"exercises": [
                    {"name": "exercise 1", "workouts": [
                        {
                            "rep": "5*2",
                            "comment": "comment comment"
                        }
                    ]},
                    {"name": "exercise 2", "workouts": []}
                ]}
            ]
        }
        self.update_program_data = {
            "name": "new name program",
            "description": "new description"
        }
        self.workouts_create_data = {
            "workouts": [
                {
                    "rep": '3*10',
                    "comment": "Feeling good",
                    "exercise_id": self.exercise.pk
                },
                {
                    "rep": '5*7',
                    "comment": "Need to improve",
                    "exercise_id": self.exercise.pk
                }
            ]
        }

    def test_programs_list(self):
        response = self.client.get(reverse('program-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_program_create(self):
        response = self.client.post(
            reverse('program-list-create'),
            self.create_program_data,
            format='json',
        )
        program = Program.objects.get(name=self.create_program_data['name'])
        serializer_data = ProgramSerializer(program).data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer_data)

    def test_program_retrieve(self):
        response = self.client.get(reverse(
            'program-retrieve-update-destroy',
            kwargs={'pk': self.program.pk}
        ))
        serializer_data = ProgramSerializer(self.program).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_program_update(self):
        response = self.client.patch(
            reverse(
                'program-retrieve-update-destroy',
                kwargs={'pk': self.program.pk},
            ),
            self.update_program_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['name'], self.update_program_data['name']
        )

    def test_program_destroy(self):
        response = self.client.delete(reverse(
            'program-retrieve-update-destroy',
            kwargs={'pk': self.program.pk},
        ))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Program.objects.filter(pk=self.program.pk))

    def test_workouts_create(self):
        response = self.client.post(
            reverse('workout-create'),
            self.workouts_create_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            len(self.exercise.workouts.all()),
            len(self.workouts_create_data['workouts']),
        )
        self.assertTrue(Workout.objects.get(
            comment=self.workouts_create_data['workouts'][0]['comment']
        ))

    def test_workout_destroy(self):
        workout = Workout.objects.create(exercise=self.exercise)
        response = self.client.delete(
            reverse('workout-destroy', kwargs={'pk': workout.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Workout.objects.filter(pk=workout.pk))
