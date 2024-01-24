from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from school.models import Schoolstore, Department, Material
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        # user = User.objects.create_user(username=username,password=password)
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('school:register')

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print("Successfully registered")
                return redirect('school:login')
        else:
            messages.info(request,"Password not matching")
            print("password error")
            return redirect('school:register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'addstudentdetail.html')


        else:
            messages.info(request,"invalid credentials")
            return redirect('login.html')
    else:
        return render(request,'login.html')
@login_required
def addstudentdetail(request, id):
    try:
        user = User.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST.get('name','')
            date_of_birth = request.POST.get('date_of_birth','')
            age = request.POST.get('age','')
            gender = request.POST.get('gender','')
            phone_number = request.POST.get('phone_number','')
            email = request.POST.get('email','')
            address = request.POST.get('address','')
            department = request.POST.get('department','')
            department_instance, created = Department.objects.get_or_create(name=department)
            courses = request.POST.get('courses','')
            purpose = request.POST.get('purpose','')
            schoolstore = Schoolstore(

                name=name,
                date_of_birth=date_of_birth,
                age=age,
                gender=gender,
                phone_number=phone_number,
                email=email,
                address=address,
                department=department_instance,
                courses=courses,
                purpose=purpose,
            )
            materials = request.POST.getlist('materials')
            for material_name in materials:
                material_instance, created = Material.objects.get_or_create(name=material_name)
                schoolstore.Materials.add(material_instance)
            schoolstore.user = user
            schoolstore.save();

            if purpose == 'placeorder':
                message = 'Order placed successfully.'
            elif purpose == 'enquiry':
                message = 'Enquiry submitted.'
            elif purpose == 'return':
                message = 'Return request submitted.'
            else:
                message = ''
            print("Before redirect",message)
            return redirect('school:success',message=message)
        # return render(request, 'index.html')
        return HttpResponse("Invalid request method. Please use POST method.")
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse("An error occurred while processing the request.")

def logout(request):
    auth.logout(request)
    return redirect('/')

def success(request, message):
    print(f"Message in success view: {message}")
    return render(request, 'success.html', {'message': message})


