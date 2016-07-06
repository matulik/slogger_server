from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from application.models import Application
import log.models

class Response(object):
    OK = 200
    UNAUTHORIZED = 400
    BADREQUEST = 404

    @staticmethod
    def getMessage(statusCode):
        if statusCode == 200:
            return u'OK'
        if statusCode == 400:
            return u'Unauthorized'
        if statusCode == 404:
            return u'Bad request'


def JSONResponse(response):
    resp = JsonResponse({'message': Response.getMessage(response)})
    resp.status_code = response
    return resp

@csrf_exempt
def addDefaultLog(request):
    if Application.authorize(request):
        print u'OK!'
        return JSONResponse(Response.OK)
    else:
        return JSONResponse(Response.UNAUTHORIZED)
