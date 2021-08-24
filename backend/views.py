from django.shortcuts import render, redirect
from .models import *
from .forms import *
import base64
from django.forms import formset_factory
from django.forms import Form
from django import forms
from django.core.files.base import ContentFile 
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def HomePage(request):
    home = Home.objects.order_by('-id')
    form = HomeForm()
    if request.method == 'POST':
        # print(request.POST)
        #print(request.POST.get("title"))
        #print(request.POST.get("image"))
        # print(request["image"])
        # print(request["title"]) 
        #print(request["Home"])
        form = HomeForm(request.POST, request.FILES or None)
        if form.is_valid():
                #image = form.cleaned_data.get('image')              
                image = form.cleaned_data['image']
                b64_img = base64.b64encode(image.file.read())
                #image_name = str(uuid.uuid4())+".jpg"
                #form.image = ContentFile(b64_img, image_name)
                

                print(request.POST)

                print("Form successfully submitted")
                print(image)
                
                #form.save()
                
    #print(message)
    context ={'form': form, 'home': home}
    return render(request, 'index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin(request):
    programmes = Allprogrammes.objects.order_by('-id')
    form = AllprogrammesForm()
    if request.method == 'POST':
        # print(request.POST)
        form = AllprogrammesForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'admin.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateadmin(request, pk):
    programme = Allprogrammes.objects.get(id=pk)
    form = AllprogrammesForm(instance=programme)
    #print('ORDER:', order)
    if request.method == 'POST':

        form = AllprogrammesForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('admin')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteadmin(request, pk):
    programme = Allprogrammes.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('admin')

    context = {'programme': programme}
    return render(request, 'admin.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def NdfulltimeView(request):
    programmes = Ndfulltime.objects.order_by('-id')
    form = NdfulltimeForm()
    if request.method == 'POST':
        # print(request.POST)
        form = NdfulltimeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'ndfulltime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatendfulltime(request, pk):
    programme = Ndfulltime.objects.get(id=pk)
    form = NdfulltimeForm(instance=programme)
    #print('ORDER:', order)
    if request.method == 'POST':

        form = NdfulltimeForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('ndfulltime')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletendfulltime(request, pk):
    programme = Ndfulltime.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('ndfulltime')

    context = {'programme': programme}
    return render(request, 'ndfulltime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def HndfulltimeView(request):
    programmes = Hndfulltime.objects.order_by('-id')
    form = HndfulltimeForm()
    if request.method == 'POST':
        # print(request.POST)
        form = HndfulltimeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'hndfulltime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatehndfulltime(request, pk):
    programme = Hndfulltime.objects.get(id=pk)
    form = HndfulltimeForm(instance=programme)
    if request.method == 'POST':

        form = HndfulltimeForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('hndfulltime')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletehndfulltime(request, pk):
    programme = Hndfulltime.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('hndfulltime')

    context = {'programme': programme}
    return render(request, 'hndfulltime.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def NdparttimeView(request):
    programmes = Ndparttime.objects.order_by('-id')
    form = NdparttimeForm()
    if request.method == 'POST':
        # print(request.POST)
        form = NdparttimeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'ndparttime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatendparttime(request, pk):
    programme = Ndparttime.objects.get(id=pk)
    form = NdfulltimeForm(instance=programme)
    if request.method == 'POST':

        form = NdfulltimeForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('ndparttime')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletendparttime(request, pk):
    programme = Ndparttime.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('ndparttime')

    context = {'programme': programme}
    return render(request, 'ndparttime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def HndparttimeView(request):
    programmes = Hndparttime.objects.order_by('-id')
    form = HndparttimeForm()
    if request.method == 'POST':
        # print(request.POST)
        form = HndparttimeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'hndparttime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatehndparttime(request, pk):
    programme = Hndparttime.objects.get(id=pk)
    form = HndparttimeForm(instance=programme)
    if request.method == 'POST':

        form = HndparttimeForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('hndparttime')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletehndparttime(request, pk):
    programme = Hndparttime.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('hndparttime')

    context = {'programme': programme}
    return render(request, 'hndparttime.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def NsukkaView(request):
    programmes = Nsukka.objects.order_by('-id')
    form = NsukkaForm()
    if request.method == 'POST':
        # print(request.POST)
        form = NsukkaForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'nsukka.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatensukka(request, pk):
    programme = Nsukka.objects.get(id=pk)
    form = NsukkaForm(instance=programme)
    if request.method == 'POST':

        form = NsukkaForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('nsukka')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletensukka(request, pk):
    programme = Nsukka.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('nsukka')

    context = {'programme': programme}
    return render(request, 'nsukka.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def CertificateView(request):
    programmes = Certificate.objects.order_by('-id')
    form = CertificateForm()
    if request.method == 'POST':
        # print(request.POST)
        form = CertificateForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'certificate.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatecertificate(request, pk):
    programme = certificate.objects.get(id=pk)
    form = CertificateForm(instance=programme)
    if request.method == 'POST':

        form = CertificateForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('certificate')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletecertificate(request, pk):
    programme = certificate.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('certificate')

    context = {'programme': programme}
    return render(request, 'certificate.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def PostgraduatesView(request):
    programmes = Postgraduates.objects.order_by('-id')
    form = PostgraduatesForm()
    if request.method == 'POST':
        # print(request.POST)
        form = PostgraduatesForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'postgraduates.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatepostgraduates(request, pk):
    programme = Postgraduates.objects.get(id=pk)
    form = PostgraduatesForm(instance=programme)
    if request.method == 'POST':

        form = PostgraduatesForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('postgraduates')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletepostgraduates(request, pk):
    programme = Postgraduates.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('postgraduates')

    context = {'programme': programme}
    return render(request, 'postgraduates.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def TutorialsView(request):
    programmes = Tutorials.objects.order_by('-id')
    form = TutorialsForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TutorialsForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'tutorials.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatetutorials(request, pk):
    programme = Tutorials.objects.get(id=pk)
    form = TutorialsForm(instance=programme)
    if request.method == 'POST':

        form = TutorialsForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('tutorials')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletetutorials(request, pk):
    programme = Tutorials.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('tutorials')

    context = {'programme': programme}
    return render(request, 'tutorials.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def CampusView(request):
    programme = Campus.objects.order_by('-id')
    form = CampusForm()
    if request.method == 'POST':
        # print(request.POST)
        form = CampusForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programme': programme, 'form': form}
    return render(request, 'campus.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatecampus(request, pk):
    programme = Campus.objects.get(id=pk)
    form = CampusForm(instance=programme)
    if request.method == 'POST':

        form = CampusForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('campusadmin')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletecampus(request, pk):
    programme = Campus.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('campusadmin')

    context = {'programme': programme}
    return render(request, 'campus.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def HostelView(request):
    programmes = Hostel.objects.order_by('-id')
    form = HostelForm()
    if request.method == 'POST':
        # print(request.POST)
        form = HostelForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'hostel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatehostel(request, pk):
    programme = Hostel.objects.get(id=pk)
    form = HostelForm(instance=programme)
    if request.method == 'POST':

        form = HostelForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('hostel')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletehostel(request, pk):
    programme = Hostel.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('hostel')

    context = {'programme': programme}
    return render(request, 'hostel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def AdmissionrequirementView(request):
    programmes = Admissionrequirement.objects.order_by('-id')
    form = AdmissionrequirementForm()
    if request.method == 'POST':
        # print(request.POST)
        form = AdmissionrequirementForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'admissionrequirement.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateadmissionrequirement(request, pk):
    programme = Admissionrequirement.objects.get(id=pk)
    form = AdmissionrequirementForm(instance=programme)
    if request.method == 'POST':

        form = AdmissionrequirementForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('admissionrequirement')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteadmissionrequirement(request, pk):
    programme = Admissionrequirement.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('admissionrequirement')

    context = {'programme': programme}
    return render(request, 'admissionrequirement.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def postutmeView(request):
    programmes = postutme.objects.order_by('-id')
    form = postutmeForm()
    if request.method == 'POST':
        # print(request.POST)
        form = postutmeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'programmes': programmes, 'form': form}
    return render(request, 'postutme.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatepostutme(request, pk):
    programme = postutme.objects.get(id=pk)
    form = postutmeForm(instance=programme)
    if request.method == 'POST':

        form = postutmeForm(
            request.POST, request.FILES or None, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('postutme')

    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletepostutme(request, pk):
    programme = postutme.objects.get(id=pk)
    if request.method == "POST":
        programme.delete()
        return redirect('postutme')

    context = {'programme': programme}
    return render(request, 'postutme.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

