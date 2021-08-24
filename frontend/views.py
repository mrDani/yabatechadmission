from django.shortcuts import render, redirect
from backend.models import *

# Create your views here.
def fehome(request):
    programme = Allprogrammes.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/index.html', context)


def fehomeblog(request, pk):
    programme = Allprogrammes.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/blog.html', context)

def fendfulltime(request):
    programme = Ndfulltime.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/ndfulltime.html', context)


def fendfulltimeblog(request, pk):
    programme = Ndfulltime.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/ndfulltimeblog.html', context)

def fehndfulltime(request):
    programme = Hndfulltime.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/hndfulltime.html', context)


def fehndfulltimeblog(request, pk):
    programme = Hndfulltime.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/hndfulltimeblog.html', context)

def fendparttime(request):
    programme = Ndparttime.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/ndparttime.html', context)


def fendparttimeblog(request, pk):
    programme = Ndparttime.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/ndparttimeblog.html', context)

def fehndparttime(request):
    programme = Hndparttime.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/hndparttime.html', context)


def fehndparttimeblog(request, pk):
    programme = Hndparttime.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/hndparttimeblog.html', context)

def fensukka(request):
    programme = Nsukka.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/nsukka.html', context)


def fensukkablog(request, pk):
    programme = Nsukka.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/nsukkablog.html', context)

def fecertificate(request):
    programme = Certificate.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/certificate.html', context)


def fecertificateblog(request, pk):
    programme = Certificate.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/certificateblog.html', context)

def fepostgraduates(request):
    programme = Postgraduates.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/postgraduates.html', context)


def fepostgraduatesblog(request, pk):
    programme = Allprogrammes.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/postgraduatesblog.html', context)

def fecampus(request):
    programme = Campus.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/campus.html', context)


def fecampusblog(request, pk):
    programme = Campus.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/campusblog.html', context)

def fetutorials(request):
    programme = Tutorials.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/tutorials.html', context)


def fetutorialsblog(request, pk):
    programme = Tutorials.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/tutorialsblog.html', context)

def fehostel(request):
    programme = Hostel.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/hostel.html', context)


def fehostelblog(request, pk):
    programme = Hostel.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/hostelblog.html', context)

def feadmissionrequirement(request):
    programme = Admissionrequirement.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/admissionrequirement.html', context)


def feadmissionrequirementblog(request, pk):
    programme = Admissionrequirement.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/admissionrequirementblog.html', context)

def fepostutme(request):
    programme = postutme.objects.order_by('-id')
    context = {'programme': programme}
    return render(request, 'frontend/postutme.html', context)


def fepostutmeblog(request, pk):
    programme = postutme.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'frontend/postutmeblog.html', context)
