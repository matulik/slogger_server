# coding=utf8

from __future__ import unicode_literals

from django.db import models

from time import time

from application.models import Application


# Enumeration for types of logs
class LogType(object):
    STANDARD = 0
    FATAL = 1
    REQUEST = 2


# Default log class
class DefaultLog(models.Model):
    application = models.ForeignKey(Application, blank=False, db_column=u'APPLICATION')
    addedDateTime = models.CharField(blank=False, editable=False, max_length=13, default=time(), db_column=u'ADDEDDATETIME')
    logValue = models.TextField()
    logType = models.IntegerField(max_length=1, blank=False, default=LogType.STANDARD, db_column=u'LOGTYPE')

    def create(self, application, logValue, logType):
        self.application = application
        self.logValue = logValue
        if logType < 0 or logType > 2:
            return False
        self.logType = logType
        self.save()
        return True


