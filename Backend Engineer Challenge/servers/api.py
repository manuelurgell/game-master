from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from app.urls import router

from players.models import Player

from servers import serializers
from servers.models import Server

from utils.mixins import BaseGenericViewSet, ListModelMixin


class ServerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    BaseGenericViewSet):

    permission_classes = (AllowAny,)
    queryset = Server.objects.all()

    serializer_class = serializers.ServerSerializer


class MatchViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    BaseGenericViewSet):

    permission_classes = (AllowAny,)

    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        region_name = self.request.query_params.get('region_name', None)

        if not region_name:
            return []

        queryset = Player.objects.filter(region_name=region_name)
        
        return queryset


router.register(
    r"servers",
    ServerViewSet,
    basename="server"
)

router.register(
    r"match",
    MatchViewSet,
    basename="match"
)
