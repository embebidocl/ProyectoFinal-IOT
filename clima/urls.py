from django.urls import path
from . import views

urlpatterns = [
    path('tiempo-real/', views.real_time_view, name='tiempo_real'),
    path('signup/', views.signup_view, name='signup'),  # <-- esta línea es nueva
]
