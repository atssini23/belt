from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import User, UserManager, Trip, TripManager

def index(request):
    all_users = User.objects.all()
    for user in all_users:
        print user.first_name, user.last_name, user.email, user.password
    return render(request, 'first_app/index.html')

def register(request):
    print request.POST
    user_manager = UserManager()
    results = user_manager.register(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'Your are now a user. Please login.')
    return redirect('/')

def login(request):
    user_manager = UserManager()
    results = user_manager.login(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        user = results['user']
        db_user = User.objects.get(first_name=user.first_name)
        request.session['first_name']= db_user.first_name
        messages.success(request, 'You have successfully logged in!')
    return redirect('/travels')

def travels(request):
    # all_trips= Trip.objects.all()
    # for trip in all_trips:
    #     print trip.destination, trip.descritption, trip.travelfrom, trip.travelto
    return render(request, 'first_app/travels.html')


def add_plan(request):
    # if request.method == 'POST':
        print request.POST
        trip_manager = TripManager()
        results = trip_manager.add_plan(request.POST)
        if not results['status']:
            for error in results['errors']:
                messages.error(request, error)
            return redirect('/travels/add')
        else:
            messages.success(request, 'Youre going on an Adventure!')
        return render(request, 'first_app/add_plan.html')
    # else:
    #     return redirect('/travels/add')
