from django.urls import path

from companies import views


app_name = 'company'
urlpatterns = [
    path('contacts/', views.CompanyContactsView.as_view(), name='contacts'),
    path('phone/list/', views.CompanyPhoneListView.as_view(), name='phone_list'),
    path('phone/add/', views.CompanyPhoneCreateView.as_view(), name='phone_add'),
    path('phone/edit/<int:pk>/', views.CompanyPhoneEditView.as_view(), name='phone_edit'),
    path('phone/delete/<int:pk>/', views.CompanyPhoneDeleteView.as_view(), name='phone_delete'),
    path('email/list/', views.CompanyEmailListView.as_view(), name='email_list'),
    path('email/add/', views.CompanyEmailCreateView.as_view(), name='email_add'),
    path('email/edit/<int:pk>/', views.CompanyEmailEditView.as_view(), name='email_edit'),
    path('email/delete/<int:pk>/', views.CompanyEmailDeleteView.as_view(), name='email_delete'),
    path('list/', views.CompanyListView.as_view(), name='list'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.CompanyEditView.as_view(), name='edit'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='detail'),
]
