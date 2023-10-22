from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist

from team.models import People, Team
from team.serializers import (
    PeopleSerializer,
    TeamSerializer,
    PeopleDetailSerializer,
    TeamUpdateSerializer
)


class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PeopleDetailSerializer
        return self.serializer_class


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return TeamUpdateSerializer
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        people_ids = request.data.get("people", [])

        for people_id in people_ids:
            try:
                people = People.objects.get(id=people_id)
                people.team = instance
            except ObjectDoesNotExist:
                return response.Response(
                    {"error": f"person with id: {people_id} does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().update(request, *args, **kwargs)

