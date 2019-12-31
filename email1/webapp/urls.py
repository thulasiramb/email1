from django.urls import path
from webapp import views
urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
    ]