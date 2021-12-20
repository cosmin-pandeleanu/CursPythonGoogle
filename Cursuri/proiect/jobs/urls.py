from django.urls import path
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.CreateJobView.as_view(), name='adaugare'),
    path('index/', views.ListJobView.as_view(), name='lista'),
    path('<int:pk>/update/', views.UpdateJobView.as_view(), name='modificare'),
    path('delete/<int:pk>/', views.delete_job, name='remove'),
]
