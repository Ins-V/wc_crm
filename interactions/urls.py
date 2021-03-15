from django.urls import path

from interactions import views


app_name = 'interaction'
urlpatterns = [
    path('list/', views.InteractionListView.as_view(), name='list'),
    path('list/my/', views.AccountInteractionListView.as_view(), name='my_list'),
    path('create/', views.InteractionCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.InteractionEditView.as_view(), name='edit'),
    path('<int:pk>/', views.InteractionDetailView.as_view(), name='detail'),
]
