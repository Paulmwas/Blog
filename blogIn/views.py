from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import BlogModel
from .forms import CreateBlog

# Create your views here.
def homePage(request):
    return render(request, 'blogIn/homePage.html')
def blogList(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blogIn/blogList.html',{'blogs':blogs})
def blogContent(request, pk):
    blogs = get_object_or_404(BlogModel, pk=pk)
    return render(request, 'blogIn/blogContent.html', {'blogs':blogs})
def blogCreate(request):
    form = CreateBlog(request.POST)
    if form.is_valid():
        newForm = form.save()
        return redirect(reverse('blogContent', args=[newForm.pk]))
    else:
        return render(request, 'blogIn/blogCreate.html', {'form':form})
def blogDelete(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blogIn/blogDelete.html', {'blog':blog})

