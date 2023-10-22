from rest_framework import serializers

from team.models import People, Team


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(many=True, required=False)

    class Meta:
        model = Team
        fields = ("id", "name", "people")


class TeamUpdateSerializer(TeamSerializer):
    people = []

    class Meta:
        model = Team
        fields = ("name", "people")
#


class PeopleDetailSerializer(PeopleSerializer):
    team = TeamSerializer()

    class Meta:
        model = People
        fields = ("id", "first_name", "last_name", "email", "team")

