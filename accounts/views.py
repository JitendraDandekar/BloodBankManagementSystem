from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.forms import modelformset_factory, inlineformset_factory
from .forms import *
from .models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request,'Invalid Credentials !!')
            return redirect('login')

    else:
        return render(request, 'login.html' )

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        termsCondins = request.POST['terms_condins']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Exist !')
                return redirect('register')

            else:
                user = Profile()
                u = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.phone = phone
                user.gender = gender
                user.terms_condins = termsCondins
                user.user = u
                user.save()
                messages.info(request, 'Profile Created !')
                return redirect('login')

    else:
        return render(request, 'registration.html')

def profile(request):
    profile = request.user.profile
    members = Member.objects.filter(profile=profile)
    return render(request, 'profile.html', {'members': members})

def editProfile(request):
    MemberFormSet = inlineformset_factory(Profile, Member, form=MemberForm, extra=3, max_num=10)
    ProfileFormSet = inlineformset_factory(User, Profile, form=ProfileForm, max_num=1)
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_formset = ProfileFormSet(request.POST, request.FILES, instance=request.user)
        member_formset = MemberFormSet(request.POST, instance=profile)
        if user_form.is_valid() and profile_formset.is_valid() and member_formset.is_valid():
            user_form.save()
            profile_formset.save()
            member_formset.save()
            messages.info(request, 'Data Updated !')
            return redirect('editprofile')
    else:
        profile_formset = ProfileFormSet(instance=request.user)
        member_formset = MemberFormSet(instance=profile)
        return render(request, 'editProfile.html', {'members':member_formset, 'profile': profile_formset})