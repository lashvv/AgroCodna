from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='/'),
    path('articles-videos/', views.articles_videos, name='articles-videos'),
    path('qa/', views.qa, name='qa'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path("logout/", views.logout_view, name="logout"),
    path('question/', views.question, name='question'),
    path('cow-calculator/', views.cow_calculator, name='cow-calculator'),
    path('soil-analyzer/', views.soil_analyzer, name='soil-analyzer'),
]