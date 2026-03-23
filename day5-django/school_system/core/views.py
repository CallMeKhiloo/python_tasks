from django.shortcuts import render
from .models import Student, Feedback
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def student_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        Student.objects.create(name=name, age=age, email=email, image=image)
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_page')

def contact_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback.objects.create(email=email, message=message)
        return redirect('home')
    return render(request, 'contact.html')