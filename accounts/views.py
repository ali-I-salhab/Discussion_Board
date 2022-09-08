from django.shortcuts import render,redirect
from boards.models import Board
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def signup(request):
    form =UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            auth_login(request=request,user=user)

            return redirect(to='home')    


    

    return render(  request=request,template_name='signup.html',context={'form' : form}) 
