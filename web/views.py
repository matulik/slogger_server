from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from application.models import Application

def home(request):
    if request.method == 'POST':
        errmsg = u'Login error. Try again.'
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return render(request, 'login.html', {'msg': errmsg})

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print str(username) + u' logged succesfully'
                return redirect('/web/applist/')
        return render(request, 'login.html', {'msg': errmsg})
    else:
        if request.user.is_authenticated():
            return render(request, 'applist.html')
        else:
            return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

@login_required
def applist(request):
    apps = Application.objects.filter(users=request.user)
    return render(request, 'applist.html', {'apps': apps})

