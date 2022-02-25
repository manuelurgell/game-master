from rest_framework import serializers

from servers.models import Server

from players.serializers import PlayerSerializer


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"
