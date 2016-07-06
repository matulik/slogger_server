# coding=utf8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from time import time
from hashlib import sha1


class Application(models.Model):
    name = models.CharField(blank=False, max_length=40, db_column=u'APP_NAME')
    token = models.CharField(blank=False, max_length=40, db_column=u'TOKEN')
    users = models.ManyToManyField(User, db_column=u'USERS')

    def __init__(self, name, users, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.name = name
        self.token = self.generatetoken()
        self.users = users

    def generatetoken(self):
        token = self.name + str(time())
        return sha1(token.encode('utf8')).hexdigest()

    def adduser(self, user):
        self.users.add(user)
