from django.shortcuts import render


from django.http import HttpResponse

def home(request):

    peoples =[
        {'name':'ahmad', 'age':18},
        {'name':'ahmad', 'age':18},
        {'name':'ahmad', 'age':18},
        {'name':'ahmad', 'age':18},
        {'name':'ahmad', 'age':18},
        {'name':'ahmad', 'age':18},
]


    return render (request,"home/index.html", {'peoples':peoples})

# def home(request):
#     return HttpResponse('This is an apple ')
