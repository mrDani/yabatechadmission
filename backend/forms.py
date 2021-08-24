from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import * 

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AllprogrammesForm(forms.ModelForm):
    class Meta:
        model = Allprogrammes                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class NdfulltimeForm(forms.ModelForm):
    class Meta:
        model = Ndfulltime                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class HndfulltimeForm(forms.ModelForm):
    class Meta:
        model = Hndfulltime                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class NdparttimeForm(forms.ModelForm):
    class Meta:
        model = Ndparttime                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class HndparttimeForm(forms.ModelForm):
    class Meta:
        model = Hndparttime                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class NsukkaForm(forms.ModelForm):
    class Meta:
        model = Nsukka                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class PostgraduatesForm(forms.ModelForm):
    class Meta:
        model = Postgraduates                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class TutorialsForm(forms.ModelForm):
    class Meta:
        model = Tutorials                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class AdmissionrequirementForm(forms.ModelForm):
    class Meta:
        model = Admissionrequirement                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }

class postutmeForm(forms.ModelForm):
    class Meta:
        model = postutme                
        fields = '__all__'
        title = forms.CharField(label="title")
        image = forms.ImageField(label="image")
        content = forms.CharField(label="content")
        widgets = {
			'content':Textarea(attrs={'cols':55, 'rows':4,'class': 'form-control','placeholder':'Enter Content Here'}),
                    }