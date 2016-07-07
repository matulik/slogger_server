from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from application.models import Application
from log.models import DefaultLog

class Response(object):
    OK = 200
    UNAUTHORIZED = 401
    BADREQUEST = 400

    @staticmethod
    def getMessage(statusCode):
        if statusCode == Response.OK:
            return u'OK'
        if statusCode == Response.UNAUTHORIZED:
            return u'Unauthorized'
        if statusCode == Response.BADREQUEST:
            return u'Bad request'


def JSONResponse(response):
    resp = JsonResponse({'status_code': response,'message': Response.getMessage(response)})
    resp.status_code = response
    return resp

@csrf_exempt
def addDefaultLog(request):
    if Application.authorize(request):

        try:
            logValue = request.POST['LOGVALUE']
            logType = request.POST['LOGTYPE']
            appName = request.POST['APPNAME']
        except KeyError:
            return JSONResponse(Response.BADREQUEST)

        try:
            app = Application.objects.get(appName=appName)
        except Application.DoesNotExist or Application.MultipleObjectsReturned:
            return JSONResponse(Response.BADREQUEST)

        if logValue and logType and appName:
            defaultLog = DefaultLog()
            if defaultLog.create(app, logValue, logType):
                return JSONResponse(Response.OK)
            else:
                return JSONResponse(Response.BADREQUEST)

    else:
        return JSONResponse(Response.UNAUTHORIZED)
