from django.db import models

class Player(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PlayerBan(models.Model):
    player_id = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='bans'
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (('player_id', 'name'),)