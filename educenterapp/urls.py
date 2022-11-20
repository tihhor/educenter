from django.urls import path
from educenterapp import views

app_name = 'educenterapp'

urlpatterns = [
    path('', views.main_page, name='index'),
    path('create/', views.create_person, name='create'),
    path('person/<int:id>/', views.person, name='person'),
    path('group/', views.group, name='group'),
    path('result/', views.result, name='result'),
    path('subject-list/', views.SubjectListView.as_view(), name='subject_list'),
    path('subject-detail/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('subject-create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject-update/<int:pk>/', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subject-delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='subject_delete'),
    path('group-list/', views.GroupListView.as_view(), name='group_list'),
    path('group-detail/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('group-create/', views.GroupCreateView.as_view(), name='group_create'),
    path('group-update/<int:pk>/', views.GroupUpdateView.as_view(), name='group_update'),
    path('group-delete/<int:pk>/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('result-list/', views.ResultListView.as_view(), name='result_list'),
    path('result-detail/<int:pk>/', views.ResultDetailView.as_view(), name='result_detail'),
    path('result-create/', views.ResultCreateView.as_view(), name='result_create'),
    path('result-update/<int:pk>/', views.ResultUpdateView.as_view(), name='result_update'),
    path('result-delete/<int:pk>/', views.ResultDeleteView.as_view(), name='result_delete'),

]
