from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_page, name='student_page'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('contact/', views.contact_us, name='contact_us'),
]