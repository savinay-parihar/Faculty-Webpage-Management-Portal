# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Profile,Qualification
from django.db import models
from . import models
from django.contrib.auth.models import User


def index(request):
    return redirect('profile/')
# Create your views here.


# def login(request):
#     next = request.GET.get('next', '/home')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=paasword)
#
#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(next)
#             else:
#                 return HttpResponse("inactive user")
#         else:
#             return render(request,"login/login.html", {'redirect_to:next'})




class UserFormView(View):
    form_class=UserForm
    template_name='registration/user_signup.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password, email=form.cleaned_data['email'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('login:index')
            return render(request,self.template_name,{'form':form})


def profile(request):
    return render(request, 'registration/faculty_home.html')



def portal(request):
    return render(request, 'registration/signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/login')


# portal views starts from here


def profile_home_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request,'login/portal_home.html')



def profile_home(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        user=request.user
        Faculty_name = request.POST['Faculty_name']
        webmail = request.POST['webmail']
        Department = request.POST['Department']
        Academic_position = request.POST['Academic_position']
        Phone = request.POST['Phone']
        RoomNo = request.POST['RoomNo']
        About = request.POST['About']
        linkedin = request.POST['linkedin']
        profile_pic= request.FILES.get('profile_pic','profile_image/400x400.png')
        fac = models.Profile.objects.filter(user=request.user)
        if not fac.exists():
            faculty = models.Profile(Faculty_name=Faculty_name,webmail=webmail,Department=Department,Academic_position=Academic_position,
                                     Phone=Phone,RoomNo=RoomNo,About=About,linkedin=linkedin,profile_pic=profile_pic,)
            faculty.user=request.user
            faculty.save()
        else:
            models.Profile.objects.filter(user=user).update(Faculty_name=Faculty_name,webmail=webmail,Department=Department,
                                                            Academic_position=Academic_position,Phone=Phone,RoomNo=RoomNo,About=About,linkedin=linkedin,profile_pic=profile_pic,)
            fac = models.Profile.objects.get(user=user)
            fac.profile_pic = profile_pic
            fac.save()

        #     Faculty_name=Faculty_name,
        #     Department=Department,
        #     Academic_position=Academic_position,
        #     Phone=Phone,
        #     RoomNo=RoomNo,
        #     linkedin=linkedin,
        #     About=About,
        #     webmail=webmail,
        #     profile_pic=profile_pic,
        # )
        return HttpResponseRedirect('/home/')




def Qualification_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request, 'login/portal_qualification.html')


def Qualification(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        Undergraduate = request.POST['Undergraduate']
        Undergraduate_college = request.POST['Undergraduate_college']
        Undergraduate_year = request.POST['Undergraduate_year']
        Postgraduate = request.POST['Postgraduate']
        Postgraduate_college = request.POST['Postgraduate_college']
        Postgraduate_year = request.POST['Postgraduate_year']
        Phd = request.POST['Phd']
        Phd_college=request.POST['Phd_college']
        Phd_year = request.POST['Phd_year']
        models.Qualification.objects.filter(user=request.user).update(
            Undergraduate = Undergraduate,
            Undergraduate_college=Undergraduate_college,
            Undergraduate_year=Undergraduate_year,
            Postgraduate = Postgraduate,
            Postgraduate_college=Postgraduate_college,
            Postgraduate_year=Postgraduate_year,
            Phd = Phd,
            Phd_college=Phd_college,
            Phd_year=Phd_year,

        )
    return HttpResponseRedirect('/home')



def Teaching_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request,'login/portal_teaching.html')



def Teaching(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        year = request.POST['year']
        semester = request.POST['semester']
        status=request.POST['status']
        Course_name = request.POST['Course_name']
      # /*  models.Teaching.objects.filter(user=request.user).append(
      #       year=year,
      #       semester=semester,
      #       Course_name=Course_name,
      #   )
        obj = models.Teaching( year=year , semester = semester , Course_name=Course_name,status=status)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect('/home/')



def Project_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request,'login/portal_project.html')



def Project(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        Title = request.POST['Title']
        Sponser = request.POST['Sponser']
        start_year = request.POST['start_year']
        end_year = request.POST['end_year']
        Role = request.POST['Role']
        Description = request.POST['Description']
        # models.Project.objects.filter(user=request.user).update(
        #     Title=Title,
        #     Sponser = Sponser,
        #     start_year = start_year,
        #     end_year = end_year,
        #     Role = Role,
        #     Description=Description,
        # )
        obj = models.Project(Title=Title , Sponser=Sponser,start_year=start_year,end_year=end_year,Role=Role,Description=Description)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect('/home/')



def Publication_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request,'login/portal_publication.html')


def Publication(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        Type = request.POST['Type']
        Title = request.POST['Title']
        Description = request.POST['Description']
        # models.Publication.objects.filter(user=request.user).update(
        #     Type=Type,
        #     Title=Title,
        #     Description=Description,
        # )
        obj = models.Publication( Type=Type, Title=Title, Description=Description)
        obj.user =  request.user
        obj.save()
        return HttpResponseRedirect('/home')


def Experience_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request,'login/portal_experience.html')

def Experience(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        start_year = request.POST['start_year']
        end_year = request.POST['end_year']
        About = request.POST['About']
        Responsibility = request.POST['Responsibility']

        obj = models.Experience(start_year=start_year, end_year=end_year, About=About, Responsibility=Responsibility)
        obj.user= request.user
        obj.save()
        return HttpResponseRedirect('/home')


# fac profile can be seen from here

def fac_home(request,username):
    # faculty = get_object_or_404(User,email = email)
    # obj2 = Qualification.objects.all()
    #obj2= Qualification.objects.filter(user=faculty )
    user = User.objects.get(username=username )
    return render(request,'registration/faculty_home.html',{'user' : user})































