from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.HomePage, name="home"),
    path('adminlogin', views.loginPage, name="login"),
    path('adminregister', views.registerPage, name="register"),
    path('adminlogout', views.logoutUser, name="logout"),

    #programmes
    path('', views.admin, name="admin"),
    path('adminupdate/<str:pk>/', views.updateadmin, name="adminupdate"),
    path('admindashboard/<str:pk>/', views.deleteadmin, name="admindelete"),

    path('ndfulltimeadmin/', views.NdfulltimeView, name="ndfulltime"),
    path('ndfulltimeupdateadmin/<str:pk>/', views.updatendfulltime, name="ndfulltimeupdate"),
    path('ndfulltimeadmin/<str:pk>/', views.deletendfulltime, name="ndfulltimedelete"),

    path('hndfulltimeadmin/', views.HndfulltimeView, name="hndfulltime"),
    path('updatehndfulltimeadmin/<str:pk>/', views.updatehndfulltime, name="updatehndfulltime"),
    path('hndfulltimeadmin/<str:pk>/', views.deletehndfulltime, name="deletehndfulltime"),

    path('ndparttimeadmin/', views.NdparttimeView, name="ndparttime"),
    path('updatendparttimeadmin/<str:pk>/', views.updatendparttime, name="updatendparttime"),
    path('ndparttimeadmin/<str:pk>/', views.deletendparttime, name="deletendparttime"),

    path('hndparttimeadmin/', views.HndparttimeView, name="hndparttime"),
    path('updatehndparttimeadmin/<str:pk>/', views.updatehndparttime, name="updatehndparttime"),
    path('hndparttimeadmin/<str:pk>/', views.deletehndparttime, name="deletehndparttime"),

    path('nsukkaadmin/', views.NsukkaView, name="nsukka"),
    path('updatensukkaadmin/<str:pk>/', views.updatensukka, name="updatensukka"),
    path('nsukkaadmin/<str:pk>/', views.deletensukka, name="deletensukka"),

    path('certificateadmin/', views.CertificateView, name="certificate"),
    path('updatecertificate/<str:pk>/', views.updatecertificate, name="updatecertificate"),
    path('certificate/<str:pk>/', views.deletecertificate, name="deletecertificate"),

    path('postgraduatesadminadmin/', views.PostgraduatesView, name="postgraduates"),
    path('updatepostgraduates/<str:pk>/', views.updatepostgraduates, name="updatepostgraduates"),
    path('postgraduates/<str:pk>/', views.deletepostgraduates, name="deletepostgraduates"),

    path('tutorialsadmin/', views.TutorialsView, name="tutorials"),
    path('updatetutorials/<str:pk>/', views.updatetutorials, name="updatetutorials"),
    path('tutorials/<str:pk>/', views.deletetutorials, name="deletetutorials"),

    path('campusadmin/', views.CampusView, name="campusadmin"),
    path('updatecampus/<str:pk>/', views.updatecampus, name="updatecampus"),
    path('campus/<str:pk>/', views.deletecampus, name="deletecampus"),

    path('hosteladmin/', views.HostelView, name="hostel"),
    path('updatehostel/<str:pk>/', views.updatehostel, name="updatehostel"),
    path('hostel/<str:pk>/', views.deletehostel, name="deletehostel"),

    path('admissionrequirementadmin/', views.AdmissionrequirementView, name="admissionrequirement"),
    path('updateadmissionrequirement/<str:pk>/', views.updateadmissionrequirement, name="updateadmissionrequirement"),
    path('admissionreuirement/<str:pk>/', views.deleteadmissionrequirement, name="deleteadmissionrequirement"),

    path('postutmeadmin/', views.postutmeView, name="postutme"),
    path('updatepostutme/<str:pk>/', views.updatepostutme, name="updatepostutme"),
    path('postutme/<str:pk>/', views.deletepostutme, name="deletepostutme"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)