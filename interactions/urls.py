from django.urls import path

from interactions import views


app_name = 'interaction'
urlpatterns = [
    path('keyword/list/', views.KeywordListView.as_view(), name='keyword_list'),
    path('keyword/add/', views.KeywordCreateView.as_view(), name='keyword_add'),
    path('keyword/edit/<int:pk>/', views.KeywordEditView.as_view(), name='keyword_edit'),
    path('keyword/delete/<int:pk>/', views.KeywordDeleteView.as_view(), name='keyword_delete'),
    path('list/', views.InteractionListView.as_view(), name='list'),
    path('list/my/', views.AccountInteractionListView.as_view(), name='my_list'),
    path('create/', views.InteractionCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.InteractionEditView.as_view(), name='edit'),
    path('<int:pk>/', views.InteractionDetailView.as_view(), name='detail'),
]
