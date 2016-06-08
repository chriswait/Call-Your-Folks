from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import *
from recommender import get_user_recommended_calls

def index(request):
    return render(request, 'callyourfolks/base.html')

def log_call(request):
    if not(request.GET.get('userId')): return HttpResponse("0") 
    userId = request.GET.get('userId')
    user = User.objects.get(id=userId)

    if not(request.GET.get('contactId')): return HttpResponse("0") 
    contactId = request.GET.get('contactId')
    contact = Contact.objects.get(id=contactId)

    if not(request.GET.get('date')): return HttpResponse("0") 
    date = request.GET.get('date')

    existing_call = Call.objects.filter(user=user, contact=contact, date=date)
    if (existing_call):
        if (existing_call[0].happened):
            return HttpResponse("0") 
        else:
            existing_call.delete()

    call = Call(user=user, contact=contact, date=date, happened=True, recommended=False)
    call.save()

    contact.generate_recommended_call()

    return HttpResponse("1")

def delete_call(request):
    if not(request.GET.get('userId')): return HttpResponse("0") 
    userId = request.GET.get('userId')
    user = User.objects.get(id=userId)

    if not(request.GET.get('contactId')): return HttpResponse("0") 
    contactId = request.GET.get('contactId')
    contact = Contact.objects.get(id=contactId)

    if not(request.GET.get('date')): return HttpResponse("0") 
    date = request.GET.get('date')

    existing_call = Call.objects.filter(user=user, contact=contact, date=date)
    if (existing_call):
        existing_call.delete()
        contact.generate_recommended_call()
        return HttpResponse("1") 
    return HttpResponse("0") 

def recommended(request):
    if not(request.GET.get('userId')): return HttpResponse("0") 
    userId = request.GET.get('userId')
    user = User.objects.get(id=userId)
    recommended_calls = get_user_recommended_calls(user)
    json = JSONRenderer().render(recommended_calls)
    return HttpResponse(json)
