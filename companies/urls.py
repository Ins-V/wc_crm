from django.urls import path

from companies import views


app_name = 'company'
urlpatterns = [
    path('list/', views.CompanyListView.as_view(), name='list'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='detail'),
]
