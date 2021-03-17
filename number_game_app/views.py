from django.shortcuts import render, redirect
import random

def index(request):
    if "answer" not in request.session:
        random.randint(1,100)
        request.session["answer"] = random.randint(1,100)
    return render(request, 'index.html')

def check_num(request):
    request.session["guess"] = int(request.POST['user_input'])
    
    if request.session["answer"] == request.session["guess"]:
        del request.session["answer"]
        request.session["message"] = "You guessed it! Keep Playing!"
        
    elif request.session["answer"] > request.session["guess"]:
        request.session["message"] = "too low!"
        
    elif request.session["answer"] < request.session["guess"]:
        request.session["message"] = "too high!"
    
    return redirect("/")
        
        
def restart(request):
    request.session.flush()
    return redirect("/")

