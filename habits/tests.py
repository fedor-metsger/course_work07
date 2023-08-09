
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            telegram='telegram_username',
            password='pbkdf2_sha256$600000$960zdQH5dHDCqHCxbD6qEM$otbdXsM6kg5daqUJYC282IO4/ddr4jcAm4WKA+dkIaI='
        )
        resp = self.client.post(
            "/token/",
            {'telegram': 'telegram_username', 'password': 'qwe123'},
            format='json'
        )
        self.token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.test_habit_data = {
            "owner": self.user,
            "action": "Test action",
            "nice": True,
            "length": 120,
            "public": True
        }
        self.habit = Habit.objects.create(**self.test_habit_data)

    def tearDown(self) -> None:
        self.habit.delete()
        self.user.delete()

    def test_habit_list(self):
        response = self.client.get(
            reverse('habit:habit_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        ret = response.json()
        self.assertEqual(ret[0], {
            "id": self.habit.id,
            "action": self.habit.action,
            "length": self.habit.length,
            "linked": None,
            "nice": self.habit.nice,
            "owner": self.user.id,
            "period": None,
            "place": None,
            "public": self.habit.public,
            "reward": None,
            "time": None
        })

    def test_habit_create(self):
        test_habit_data = {
            "owner": self.user.id,
            "linked": 1,
            "action": "Test action",
            "nice": False,
            "length": 120,
            "period": 7,
            "place": "Дома",
            "public": True,
            "reward": ""
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            test_habit_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            2,
            Habit.objects.all().count()
        )

    def test_habit_patch(self):
        test_habit_data = {
            "public": False
        }

        response = self.client.patch(
            reverse('habit:habit_update', args=[self.habit.pk]),
            test_habit_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.habit.refresh_from_db()
        self.assertEqual(
            self.habit.public,
            test_habit_data["public"]
        )

    def test_habit_delete(self):
        habit_id = self.habit.pk
        response = self.client.delete(
            reverse('habit:habit_destroy', args=[habit_id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Habit.objects.filter(pk=habit_id).exists(),
            False
        )
