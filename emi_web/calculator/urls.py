from django.urls import path
from . import views
from . import verification_views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('googleb66a2a1986aafb83.html', verification_views.google_verification_view, name='google_verify'),
    path('robots.txt', verification_views.robots_txt_view, name='robots_txt'),
]
