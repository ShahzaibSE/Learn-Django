from django.shortcuts import render, HttpResponse;
from django.http import JsonResponse;
from .models import Question;
from django.core import serializers;

# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def voters(request):
    return JsonResponse(serializers.serialize('json', Question.objects.all()), safe=False);