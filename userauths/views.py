from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from userauths.models import User,Profile
from userauths.forms import UserRegisterForm



# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f'You are already logged in.')
    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        
        user = authenticate(email=email, password=password) 
        login(request,user)

        messages.success(request, f"Account created for {full_name}! You are now logged in.")
        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name 
        profile.phone = phone 
        profile.save()

        return redirect( "hotel:index")

    context = {
        "form": form
    }
    return render(request,"userauths/sign-up.html", context)



def loginViewTemp(request):

    if request.user.is_authenticated:
        messages.warning(request, f'You are already logged in.')
        return redirect("hotel:index")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_query = User.objects.get(email=email)
            user_auth = authenticate(request, email=email, password=password) 

            if user_query is not None:
                login(request, user_auth)
                messages.success(request, f"You are logged in")
                next_url = request.GET.get("next", "hotel:index")
                return redirect(next_url)
            else:
                messages.error(request, f'Username or password does not exist')
                return redirect("userauths:sign-in")
            
        except:
            messages.error(request, f'User does not exist')
            return redirect("userauths:sign-in")
                

    return render(request,"userauths/sign-in.html")


def LogoutView(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("hotel:index")