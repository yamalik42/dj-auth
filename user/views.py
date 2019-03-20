from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth import authenticate, logout


# Create your views here.
def check_user(request):
    user_dict = {
        2: 'is super',
        1: 'is staff',
        0: 'is anonymous'
    }

    user = request.user
    map_user = user.is_superuser + user.is_staff

    response = HttpResponse(user_dict[map_user])

    return response


def logout_view(request):
    name = request.user.username
    logout(request)

    logout_dict = {
        True: name,
        False: 'Nobody'
    }

    res_str = logout_dict[bool(len(name))]

    return HttpResponse(f'{res_str} was logged out.')
