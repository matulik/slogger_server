# coding=utf8

from __future__ import unicode_literals

from django.db import models

from time import time
from datetime import datetime

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

    def as_json(self):
        return {
            "id": self.id,
            "addedDateTime": datetime.fromtimestamp(float(self.addedDateTime)).strftime('%Y-%m-%d %H:%M:%S'),
            "logType": self.logType,
            "logValue": self.logValue
        }

    def create(self, application, logValue, logType):
        try:
            logValueInt = int(logType)
        except:
            return False
        if logValueInt < 0 or logValueInt > 2:
            return False
        self.application = application
        self.logValue = logValue
        self.logType = logType
        self.save()
        return True


