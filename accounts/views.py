from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.forms import modelformset_factory, inlineformset_factory
from .forms import *
from .models import *
from availibility.forms import *
from availibility.models import *

#Decorator
def user_is_staff(func):
    def staff_checker(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('<h1>Unauthorized Access</h1>')
    return staff_checker



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
            messages.info(request, 'Password Not Matched !')
            return redirect('register')


    else:
        return render(request, 'registration.html')


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile
    members = Member.objects.filter(profile=profile)
    return render(request, 'profile.html', {'members': members})

def my_donation(request):
    donation_form = DonationForm()
    req_details = BloodRequest.objects.filter(user=request.user)
    my_donations = Donation.objects.filter(user=request.user)
    donation_count = my_donations.count()  
    req_count = req_details.count()
    if request.method == 'POST':
        donation_form = DonationForm(request.POST, request.FILES)
        if donation_form.is_valid():
            df = donation_form.save(commit=False)
            df.user = request.user
            df.save()
            messages.info(request, 'Saved !')
            return redirect('mydonation')
    else:
        return render(request, 'myDonation.html',{'reqcount':req_count, 'reqdetails':req_details,
         'mydonations':my_donations, 'donationcount':donation_count, 'donationform':donation_form})

@login_required(login_url='login')
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


@login_required(login_url='login')
@user_is_staff
def admin_panel(request):
    users = User.objects.all()
    blood_status = BloodAvailibility.objects.all()
    care_centres = CareCentre.objects.all()
    camp_details = Camp.objects.all()
    blood_request = BloodRequest.objects.raw('select id, user_id,count(*) as ucount from accounts_bloodrequest GROUP BY user_id order by req_date desc')
    return render(request, 'adminpanel.html', {'bloodstatus':blood_status, 'carecentres':care_centres,
     'campdetails':camp_details, 'users':users, 'bloodrequest':blood_request})

def request_panel(request, pk):
    blood_request = BloodRequest.objects.filter(user_id=pk).order_by('-req_date')
    return render(request, 'request.html', {'bloodrequest':blood_request})


@user_is_staff
def user_profile(request, pk):
    user = User.objects.filter(id=pk)
    u = User.objects.get(id=pk)
    usersFormSet = modelformset_factory(User, form=AdminPanelUserForm, extra=0)
    profileFormSet = inlineformset_factory(User, Profile, form=AdminPanelProfileForm, can_delete=True)
    memberFormSet = inlineformset_factory(Profile, Member, form=AdminPanelMemberForm, can_delete=True)
    if request.method == 'POST':
        users = usersFormSet(request.POST, queryset=user)
        profile = profileFormSet(request.POST, request.FILES, instance=u)
        members = memberFormSet(request.POST, instance=u.profile)
        if users.is_valid() and profile.is_valid() and members.is_valid():
            user = users.save()
            profile.save()
            members.save()
            messages.info(request, 'Data Updated !')
            return redirect('userprofile', pk)
    else:
        users = usersFormSet(queryset=user)
        profile = profileFormSet(instance=u)
        members = memberFormSet(instance=u.profile)
        return render(request, 'userProfile.html', {'users':users, 'profile':profile, 'members':members})

@user_is_staff
def edit_panel(request, field, pk):
    if field == 'bloods':
        b_id = BloodAvailibility.objects.filter(id=pk)
        bloodStatusFormSet = modelformset_factory(BloodAvailibility, form=BloodAvailibilityForm, can_delete=True, extra=0)
        if request.method == 'POST':
            blood_status = bloodStatusFormSet(request.POST, queryset=b_id)
            if blood_status.is_valid():
                blood_status.save()
                messages.info(request, 'Data Updated !')
                return redirect('editpanel', field, pk)
        else:
            blood_status = bloodStatusFormSet(queryset=b_id)
            return render(request, 'updatePanel.html', {'bloodstatus':blood_status})
    
    elif field == 'camps':
        c_id = Camp.objects.filter(id=pk)
        campFormSet = modelformset_factory(Camp, form=CampConfirmationForm, can_delete=True, extra=0)
        if request.method == 'POST':
            camp_details = campFormSet(request.POST, queryset=c_id)
            if camp_details.is_valid():
                camp_details.save()
                messages.info(request, 'Data Updated !')
                return redirect('editpanel', field, pk)
        else:
            camp_details = campFormSet(queryset=c_id)
            return render(request, 'updatePanel.html', {'campdetails':camp_details})

    elif field == 'centre':
        care_id = CareCentre.objects.filter(id=pk)
        careCentreFormSet = modelformset_factory(CareCentre, form=CareCentreForm, can_delete=True, extra=0)
        if request.method == 'POST':
            care_centre = careCentreFormSet(request.POST, queryset=care_id)
            if care_centre.is_valid():
                care_centre.save()
                messages.info(request, 'Data Updated !')
                return redirect('editpanel', field, pk)

        else:
            care_centre = careCentreFormSet(queryset=care_id)
            return render(request, 'updatePanel.html', {'carecentres':care_centre})

@user_is_staff
def delete(request, field, pk):
    if field == 'bloods':
        BloodAvailibility.objects.get(id=pk).delete()
        messages.info(request, 'Deleted !')
        return redirect('adminpanel')

    elif field == 'camps':
        Camp.objects.get(id=pk).delete()
        messages.info(request, 'Deleted !')
        return redirect('adminpanel')

    elif field == 'centre':
        CareCentre.objects.get(id=pk).delete()
        messages.info(request, 'Deleted !')
        return redirect('adminpanel')

def blood_request(request):
    members = Member.objects.filter(profile=request.user.profile)
    blood_request = BloodRequestForm()
    if request.method == 'POST':
        member = request.POST['members']
        print(member)
        blood_request = BloodRequestForm(request.POST)
        if blood_request.is_valid():
            print(blood_request)
            br = blood_request.save(commit=False)
            br.user = request.user
            br.request_for = Member.objects.get(full_name=member)
            br.save()
            messages.info(request, 'Request proceeding !')
            return redirect('bloodrequest')
    else:
        return render(request, 'bloodRequest.html', {'bloodrequest': blood_request, 'members':members})