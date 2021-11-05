from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .models import Profile


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('profiles')

        else:
            messages.success(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userprofile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    topskills = user_profile.skill_set.exclude(description__exact="").order_by("priority")
    otherskills = user_profile.skill_set.filter(description="")
    context = {
        'user_profile': user_profile,
        'topskills': topskills,
        'otherskills': otherskills,
    }
    return render(request, 'users/userprofile.html', context)


@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile

    topskills = profile.skill_set.exclude(description__exact="").order_by("priority")
    otherskills = profile.skill_set.filter(description="")
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'topskills': topskills,
        'otherskills': otherskills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url="login")
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url="login")
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url="login")
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')

    context = {'object': skill}
    return render(request, 'users/delete_template.html', context)
