# coding=utf8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from time import time
from datetime import datetime
from hashlib import sha1


class Application(models.Model):
    appName = models.CharField(blank=False, max_length=40, db_column=u'APP_NAME')
    createdDate = models.CharField(blank=False, editable=False, max_length=13, db_column=u'CREATEDDATE')
    token = models.CharField(blank=False, max_length=40, db_column=u'TOKEN')
    users = models.ForeignKey(User, db_column=u'USERS')

    def create(self, name, users):
        _time = time()

        self.appName = name
        self.createdDate = _time
        self.users = users
        self.token = Application.generatetoken(name, _time)

        self.save()

    def adduser(self, user):
        self.users.add(user)

    def getFormatedCreatedDate(self):
        return datetime.fromtimestamp(float(self.createdDate)).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def generatetoken(name, time):
        token = name + str(time)
        return sha1(token.encode('utf8')).hexdigest()

    @staticmethod
    def authorize(request):
        if request.method != 'POST':
            return False

        try:
            appName = request.POST['APPNAME']
            token = request.META['HTTP_TOKEN']
        except KeyError:
            return False

        if not token or not appName:
            return False

        try:
            authApp = Application.objects.get(appName=appName)
        except Application.DoesNotExist or Application.MultipleObjectsReturned:
            return False

        if authApp.token == token:
            return True
        else:
            return False
