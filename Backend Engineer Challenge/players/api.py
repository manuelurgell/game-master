from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from app.urls import router
from players import serializers
from players.models import Player
from utils.mixins import BaseGenericViewSet, ListModelMixin


class PlayerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    BaseGenericViewSet):

    permission_classes = (AllowAny,)
    queryset = Player.objects.all()

    serializer_class = serializers.PlayerSerializer


router.register(
    r"players",
    PlayerViewSet,
    basename="player"
)

router.register(
    r"players",
    PlayerViewSet,
    basename="player"
)
