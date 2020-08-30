from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import user, crk, crk2

def login(request):
    if request.method == "GET":
        return render(request, "exam/login.html")
    else:
        surname = request.POST["surname"]
        firstname = request.POST["firstname"]
        othername = request.POST["othername"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        score = 0
        username = (surname+" "+firstname+" "+othername)
        try:
            user_idd = user.objects.get(username = username)
        except:
            return render(request, "exam/submit.html", {
                "message": "Hello, sorry we couldnt access any registrant with your details. Kindly ensure all inputs are correct!"
            })
        if user_idd.scoreagric != 0:
            return render(request, "exam/submit.html", {
                "message": "Hello, it seems you're trying to resubmit for the exam. The entry is only once!"
            })
        user_id = user_idd.id
        return HttpResponseRedirect(reverse("index", args=(user_id,)))


def index(request, user_id):
    if request.method == "GET":
        #return HttpResponse(user_id)
        user_idd = user.objects.get(id = user_id)
        mathsi = crk.objects.all()
        mathsii = crk2.objects.all()
        #return HttpResponse(user_idd)
        return render(request, "exam/index.html", {
            "user": user_idd,
            "mathsi": mathsi,
            "mathsii": mathsii
        })
    else:
        score = request.POST["score"]

        user_idd = user.objects.get(id = user_id)
        user_idd.scorecrs = score
        user_idd.save()

        return render(request, "exam/submit.html", {
            "message" : "Congratulations! your exam has been submitted successfully. Quietly exit your sit for the next Candidate"
        })
