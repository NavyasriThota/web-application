from django.urls import path

from . import views

urlpatterns = [
    path('', views.hr_list, name='hr_list'),
    path('new/', views.hr_create, name='hr_create'),
    path('<int:pk>/', views.hr_detail, name='hr_detail'),
    path('<int:pk>/edit/', views.hr_update, name='hr_update'),
    path('<int:pk>/delete/', views.hr_delete, name='hr_delete'),
]
