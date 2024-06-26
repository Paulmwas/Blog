from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage, name='home'),
    path('blog/', views.blogList, name='blogs')
]
