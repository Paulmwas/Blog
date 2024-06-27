from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage, name='home'),
    path('blog/', views.blogList, name='blogs'),
    path('blog/<int:pk>/', views.blogContent, name='blogContent'),
    path('createblog/',views.blogCreate,name='createBlog'),
    path('blog/<int:pk>/delete/', views.blogDelete, name='delete')
]
