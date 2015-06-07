
from django.shortcuts import render

def login_view(request, next=None):
    return render(request, 'wevote_social/login.html', {'next': next})
