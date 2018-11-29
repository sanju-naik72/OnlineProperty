from django.db import models


class State(models.Model):
    id_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

