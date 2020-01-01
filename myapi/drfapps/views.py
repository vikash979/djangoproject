from django.shortcuts import render

# Create your views here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapps.templates.form import EmpForm,StudentForm
from myapps.functions.functions import handle_uploaded_file
from  myapps.models import Student

@login_required
def index(request):
   print(request)
   #template = loader.get_template('myapps/index.html') # getting our template
   stu = StudentForm()
   name = {
       'student': 'rahul',
       'form':stu

   }

   return render(request, 'drfapps/index.html', name)

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def acti(request):
    if request.method == "POST":

        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print("##############",request.FILES['file'])
            handle_uploaded_file(request.FILES['file'])

            try:
                #print(form)
                Movies_List=Student.objects.create(first_name=request.POST.get('firstname'),last_name=request.POST.get('lastname'))
                return redirect('/')
            except:
                print("kumar")
                pass
        else:
            print("aaaaaaaaaaaaaa")
                # if request.method == "POST":
    #     form = EmployeeForm(request.POST)
    return render(request, 'acti.html', {'form': "form"})


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)