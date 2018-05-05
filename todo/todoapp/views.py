from django.shortcuts import render, HttpResponse;

def tododetail(request, todo_id):
    return HttpResponse("You're looking at todo %s." % todo_id);
