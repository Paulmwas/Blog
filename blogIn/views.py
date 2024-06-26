from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def homePage(request):
    return render(request, 'blogIn/homePage.html')
def blogList(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blogIn/blogList.html',{'blogs':blogs})