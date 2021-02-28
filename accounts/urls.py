from django.urls import path

from accounts import views


app_name = 'account'
urlpatterns = [
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.LoginView.as_view(), name='login'),
]
