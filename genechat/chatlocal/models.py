# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.text

