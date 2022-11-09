from django.urls import path
from educenterapp import views

app_name = 'educenterapp'

urlpatterns = [
    path('', views.main_page, name='index'),
    path('create/', views.create_person, name='create'),
    path('person/<int:id>/', views.person, name='person'),
]
