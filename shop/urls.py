from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name= 'about'),
    path('services/', views.services, name= 'services'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('blog/', views.blog, name= 'blog'),
    path('contact/', views.contact, name= 'contact'),
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book, name='book'),
]