from django.urls import path

from companies import views


app_name = 'company'
urlpatterns = [
    path('list/', views.CompanyListView.as_view(), name='list'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.CompanyEditView.as_view(), name='edit'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='detail'),
]
