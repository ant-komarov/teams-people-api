from django.urls import path, include
from rest_framework import routers

from team.views import PeopleViewSet, TeamViewSet

router = routers.DefaultRouter()
router.register("people", PeopleViewSet)
router.register("teams", TeamViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "team"
