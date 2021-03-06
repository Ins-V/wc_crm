from django.urls import path

from accounts import views


app_name = 'account'
urlpatterns = [
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password/change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('account/', views.AccountDetailView.as_view(), name='detail'),
    path('settings/', views.AccountSettingsView.as_view(), name='settings'),
    path('', views.LoginView.as_view(), name='login'),
]
