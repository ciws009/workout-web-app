from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.workout_record, name='workout_record'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup')
]
