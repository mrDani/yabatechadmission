from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.fehome, name="fehome"),
    path('homeblog/<str:pk>/', views.fehomeblog, name="fehomeblog"),
    path('ndfulltime/', views.fendfulltime, name="fendfulltime"),
    path('ndfulltime/<str:pk>/', views.fendfulltimeblog, name="fendfulltimeblog"),
    path('hndfulltime/', views.fehndfulltime, name="fehndfulltime"),
    path('hndfulltime/<str:pk>/', views.fehndfulltimeblog, name="fehndfulltimeblog"),
    path('ndparttime', views.fendparttime, name="fendparttime"),
    path('ndparttime/<str:pk>/', views.fendparttimeblog, name="fendparttimeblog"),
    path('hndparttime/', views.fehndparttime, name="fehndparttime"),
    path('hndparttime/<str:pk>/', views.fehndparttime, name="feparttimeblog"),
    path('nsukka/', views.fensukka, name="fensukka"),
    path('nsukka/<str:pk>/', views.fensukka, name="fensukkablog"),
    path('certificate/', views.fecertificate, name="fecertificate"),
    path('certificate/<str:pk>/', views.fecertificateblog, name="fecertificateblog"),
    path('postgraduate/s', views.fepostgraduates, name="fepostgraduates"),
    path('postgraduates/<str:pk>/', views.fepostgraduatesblog, name="fepostgraduatesblog"),
    path('tutorials/', views.fetutorials, name="fetutorials"),
    path('tutorials/<str:pk>/', views.fetutorialsblog, name="fetutorialsblog"),
    path('campus/', views.fecampus, name="fecampus"),
    path('campus/<str:pk>/', views.fecampusblog, name="fecampusblog"),
    path('hostel/', views.fehostel, name="fehostel"),
    path('hostel/<str:pk>/', views.fehostelblog, name="fehostelblog"),
    path('admissionrequirement/', views.feadmissionrequirement, name="feadmissionrequirement"),
    path('admissionrequirement/<str:pk>/', views.feadmissionrequirementblog, name="feadmissionrequirementblog"),
    path('postutme/', views.fepostutme, name="fepostutme"),
    path('postutme/<str:pk>/', views.fepostutmeblog, name="fepostutmeblog"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)