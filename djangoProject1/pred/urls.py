from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import  views

urlpatterns = [
    path('', views.my_login , name = 'login'),
    path('predict/', views.predict , name= 'predict'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('dashboarddesktop/',views.dashboarddesktop, name = 'dashboarddesktop'),
    path('dashboardsmartphone/',views.dashboardsmartphone, name = 'dashboardsmartphone'),
    path('register/', registerForm, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('comp/<str:f>/', views.comp, name='comp'),
    path('desktop/', views.comp_burreau, name='desktop'),
    path('smartphone/<str:f>/', views.comp_smartphone, name='smartphone'),
    path('affiche/<str:ref>/',views.affiche , name='affiche' ),
    path('afficheburreau/<str:ref>/',views.affiche_burreau , name='afficheburreau' ),
    path('res/', views.res , name='res'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)