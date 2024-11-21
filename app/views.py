from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# index page view
def IndexPage(request):
    reviews = testimonials.objects.all()
    return render(request, "app/index.html",{'reviews':reviews})

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def services(request):
    return render(request, "app/services.html")

def porojects(request):
    allProjects = projects.objects.all()
    return render(request, "app/porojects.html",{'project':allProjects})




# // views for subscribe
def Subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        user = subscribe.objects.filter(email=email)
        if user:
            message = "You alrady subscribed."
            return render(request, "app/index.html",{'msg':message})
        else:
            subscribe.objects.create(email=email)
            return redirect('index')
  

####---- admin site views ----- ####


def adminIndex(request):
    allProjects = projects.objects.all()
    reviews = testimonials.objects.all()
    return render(request, "app/admin/index.html",{'reviews':reviews, 'project':allProjects})

def LoginPage(request):
    return render(request, "app/admin/pages-sign-in.html")

# // update status
def accept(request):
    return render(request, "app/admin/accept.html")

def testomonialPage(request):
    return render(request, "app/testomonial.html")

def addProjectsPage(request):
    return render(request, "app/addProjects.html")



def adminLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email == "adminy":
            if password == "adminy":

                request.session['email'] = email
                request.session['password'] = password

                return redirect('adminIndex')
            else:
                message = "Bhai password bhul"
                return render(request, "app/admin/pages-sign-in.html", {'msg':message})
        else:
            message = "Bhai email bhul"
            return render(request, "app/admin/pages-sign-in.html", {'msg':message})



    return render(request, "app/admin/pages-sign-in.html")

#// Get Testimonial 
def GetTestimonial(request):
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        newReview = testimonials.objects.create(
            name=name,
            title=title,
            description=description,
            image=image,
        )
        return render(request, "app/index.html")

#// Upload a project
def upProject(request):
    if request.method == "POST":
        proName = request.POST['proName']
        proTitle = request.POST['proTitle']
        description = request.POST['description']
        live = request.POST['live']
        cover = request.FILES['cover']

        newProjects = projects.objects.create(
            proName=proName,
            proTitle=proTitle,
            description=description,
            live=live,
            cover=cover,
        )
        return render(request, "app/admin/index.html")