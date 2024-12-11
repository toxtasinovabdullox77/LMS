from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_list, name='course_list'),  # Kurslar ro‘yxati
    path('<int:pk>/', views.course_detail, name='course_detail'),  # Kurs tafsilotlari
]
