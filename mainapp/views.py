from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,
        'index.html')

def about(request):
    return render(request,
        'about.html')

def blog_single(request):
    return render(request,
        'blog-single.html')

def blog(request):
    return render( request, 
        "blog.html"
    )

def contact(request):
    return render( request,
       " contact.html")

def portfolio(request):
    return render( request , 
        "portfolio.html"
    )
def portfolio_details(request):
    return render( request, 
        "portfolio-details.html"
    )
def services(request):
    return render( request, "services.html")

def team(request):
    return render(request, "team.html")
def contact(request):
    return render(request, "contact.html")
