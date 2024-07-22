from django.shortcuts import redirect, render
from vege.models import Receipes, Student, SubjectMarks
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Sum, F, Window
from django.db.models.functions import Rank
from .models import SubjectMarks, Student

# Create your views here.

@login_required(login_url="/login")
def receipe(request):
    if request.method == "POST":
      data = request.POST
      receipes_name = data.get("receipes_name")
      public = data.get("public")
      
      receipes_discription = data.get("receipes_discription")
      receipes_image = request.FILES["receipes_image"]

      if public == "Private":
        
        new_recipe = Receipes.objects.create(
        receipes_discription = receipes_discription,
        receipes_name = receipes_name,
        receipes_image = receipes_image,
        )
        
        new_recipe.public_private.add (request.user)
        return redirect("/receipes/")
      if public == "Public":
        new_recipe = Receipes.objects.create(
         receipes_discription = receipes_discription,
         receipes_name = receipes_name,
         receipes_image = receipes_image,
        )
        for i in User.objects.all():
            new_recipe.public_private.add(i)
        return redirect("/receipes/")
    queryset = Receipes.objects.filter(public_private=request.user)
    context = {"receipes": queryset}

    # if request.GET.get('search'):
    #     queryset = queryset.filter(receipes_name_icontain = request.GET.get('search'))
        

    



 
   

    return render(request ,'vege/receipes.html',context)
# def home(request):
def update_receipe(request, id):
    queryset = Receipes.objects.get(id = id)

    
    if request.method == "POST":
        receipes_name = request.POST.get("receipes_name")
        receipes_discription = request.POST.get("receipes_discription")
       
        receipes_image = request.FILES.get("receipes_image")
        
        if receipes_name:
            queryset.receipes_name = receipes_name
            
        if receipes_discription:   
            queryset.receipes_discription = receipes_discription
        
        if receipes_image:
            queryset.receipes_image = receipes_image
        
        
        queryset.save()
        
       
        return redirect("/receipes/")
    
   
    context = {"receipe": queryset}
    return render(request, 'vege/update_receipes.html', context)

def login_tty(request):
    print(request.user)
    if request.method == 'POST':
       username=request.POST.get('username')
       Password=request.POST.get('Password')

       print(username)
       print(Password)
       if not User.objects.filter(username = username).exists():
           messages.error(request, "invalid user name.")
       
       user = authenticate (username = username , password = Password)


       if  user is None :
           messages.error(request, "invalid user name.")
           return redirect('/login/')
       else:
           login(request ,user)
           return redirect('/receipes/')
       




    return render(request , 'vege/login.html')

def logout_page(request):
    logout(request)
    return  redirect("/login")

   

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        Password=request.POST.get("Password")

        user = User.objects.filter(username = username)
        if user.exists():
         messages.info(request, "username is already taken.")
         return redirect('/register/')

        user = User.objects.create(
            username = username,
            first_name = first_name, 
            last_name = last_name, 
                                  )
        user.set_password(Password)
        user.save()
        messages.info(request, "account created.")
        return redirect('login')

    print("Register")
    return render(request , 'vege/register.html')


def delete_receipe(request, id):
   queryset = Receipes.objects.get(id = id)
   queryset.delete()
   return redirect('receipes')
 

def get_students(request):
   queryset =Student.objects.all()
   
   

   paginator = Paginator(queryset, 2)  # Show 25 contacts per page.

   page_number = request.GET.get("page",1)
   page_obj = paginator.get_page(page_number)
   

   return render( request , "vege/students.html" , {"queryset" : page_obj})




















def see_marks(request, student_id):
    # Query the marks for the given student
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id )
    total_marks = queryset.aggregate(total_marks=Sum("marks"))

    # Annotate each student with their total marks and rank them
    ranks = Student.objects.annotate(
        total_marks=Sum('studentmarks__marks'),
        rank=Window(
            expression=Rank(),
            order_by=[F('total_marks').desc()]
        )
    )

    # Get the rank and details of the current student
    current_rank = -1
    student_name = ''
    
    for rank in ranks:
        if student_id == rank.student_id:
            current_rank = rank.rank
            student_name = rank.name  # Assuming 'name' is a field in the Student model
            break
        

    return render(request, "vege/see_marks.html", {
        "queryset": queryset,
        'total_marks': total_marks,
        "current_rank": current_rank,
        "student_name": student_name,
    })











# def see_marks(request , student_id):
#    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id )
#    total_marks = queryset.aggregate(total_marks = Sum ("marks"))
#    current_rank = -1
#    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , '-student_age')
   

#    i = 1

#    for rank in ranks:
#         if student_id == rank.student_id.student_id:
#            current_rank = i
#            break
#         i  = i + 1
      
#    return render( request , "vege/see_marks.html" , {"queryset" : queryset  , 'total_marks' : total_marks  , " current_rank" :  current_rank})



    

  
  