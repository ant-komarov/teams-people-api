from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from team.models import Team, People


def person_sample(person_data: dict) -> People:
    return People.objects.create(**person_data)


def team_sample(team_data: dict) -> Team:
    return Team.objects.create(**team_data)


class TeamCreateApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_team_create(self):
        payload = {
            "name": "Alpha"
        }

        response = self.client.post(reverse("team:team-list"), payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        team = Team.objects.get(id=response.data["id"])

        self.assertEqual(payload["name"], team.name)


class TeamUpdateApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        person_data1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "doe@mail.com"
        }
        person_data2 = {
            "first_name": "Ava",
            "last_name": "Page",
            "email": "page@mail.com"
        }
        team_data = {
            "name": "Alpha"
        }
        self.person1 = person_sample(person_data1)
        self.person2 = person_sample(person_data2)
        self.team = team_sample(team_data)
        self.url = reverse("team:team-detail", args=[self.team.id])

    def test_assign_person_to_team(self):

        data = {"people": [1]}

        response = self.client.patch(self.url, data)

        self.team.refresh_from_db()
        self.person1.refresh_from_db()
        self.person2.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.team.name, self.person1.team.name)
        self.assertEqual(self.person2.team, None)

    def test_reassign_people_to_team(self):

        self.person1.team = self.team

        data = {"people": [2]}

        response = self.client.patch(self.url, data)

        self.team.refresh_from_db()
        self.person1.refresh_from_db()
        self.person2.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.team.name, self.person2.team.name)
        self.assertEqual(self.person1.team, None)

    def test_multiple_assign_people_to_team(self):

        data = {"people": [1, 2]}

        response = self.client.patch(self.url, data)

        self.team.refresh_from_db()
        self.person1.refresh_from_db()
        self.person2.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.team.name, self.person1.team.name)
        self.assertEqual(self.team.name, self.person2.team.name)

    def test_assign_person_with_wrong_id(self):

        data = {"people": [1, 2, 3]}

        message = {"error": "person with id: 3 does not exist"}

        response = self.client.patch(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, message)
