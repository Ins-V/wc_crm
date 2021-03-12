from django.urls import path

from projects import views


app_name = 'project'
urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='list'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.ProjectEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
]
