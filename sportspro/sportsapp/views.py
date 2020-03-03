from django.shortcuts import render
from .forms import RegistrationForm,LoginForm,MrecordForm,ReportForm
from .models import RegistrationData,MrecordData,ReportData
from django.http.response import HttpResponse
from .import forms

def main_page(request):
    return render(request,'base.html')

def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username','')
            pwd = request.POST.get('password1','')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password1=pwd)
            if uname1 and pwd1:
                return HttpResponse("valid details")
            else:
                return HttpResponse("invalid details")

    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})


def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            #typeof_register = request.POST.get('typeof_register','')
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            mobile = request.POST.get('mobile','')
            email = request.POST.get('email','')
            username = request.POST.get('username','')
            password1 = request.POST.get('password1','')
            password2 = request.POST.get('password2','')
            age = request.POST.get('age','')
            data=RegistrationData(
                #typeof_register=typeof_register,
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                email=email,
                username=username,
                password1=password1,
                password2=password2,
                age=age,
            )
            data.save()
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})
    else:
        rform=RegistrationForm()
        return render(request,'registration.html',{'rform':rform})


def mrecord_view(request):
    if request.method == "POST":
        mform = MrecordForm(request.POST)
        if mform.is_valid():
            match_name = request.POST.get('match_name','')
            match_status = request.POST.get('match_status','')
            match_coach = request.POST.get('match_coach','')
            match_umpire = request.POST.get('match_umpire','')
            match_number = request.POST.get('match_number','')
            data=MrecordData(
                match_name=match_name,
                match_status=match_status,
                match_coach=match_coach,
                match_umpire=match_umpire,
                match_number=match_number,
            )
            data.save()
        mform=MrecordForm()
        return render(request,'mrecord.html',{'mform':mform})
    else:
        mform = MrecordForm()
        return render(request,'mrecord.html', {'mform': mform})
def report_view(request):
    if request.method == "POST":
        tform = ReportForm(request.POST)
        if tform.is_valid():
            report_name = request.POST.get('report_name','')
            report_status = request.POST.get('report_status','')
            report_coach = request.POST.get('report_coach','')
            report_umpire = request.POST.get('report_umpire','')
            data=ReportData(
                report_name=report_name,
                report_status=report_status,
                report_coach=report_coach,
                report_umpire=report_umpire,
            )
            data.save()
        tform=ReportForm()
        return render(request,'report.html',{'tform':tform})
    else:
        tform = ReportForm()
        return render(request, 'report.html', {'tform': tform})


