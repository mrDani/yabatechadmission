from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()


    class Meta:
        db_table = 'home'

class Allprogrammes(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()


    class Meta:
        db_table = 'Allprogrammes'

class Ndfulltime(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'ndfulltime'

class Hndfulltime(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'hndfulltime'

class Ndparttime(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'ndparttime'

class Hndparttime(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'hndparttime'

class Nsukka(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'nsukka'

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'certificate'

class Postgraduates(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'postgraduates'

class Tutorials(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'tutorials'

class Campus(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'campus'

class Hostel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'hostel'

class Admissionrequirement(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'Admissionrequirement'

class postutme(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'postutme'

class Test(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'test'
