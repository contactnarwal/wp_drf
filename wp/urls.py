from django.urls import path
from .views import RegisterView, UserListView, UserDetailView, UserUpdateView,UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
     path('users/<int:id>/update/', UserUpdateView.as_view(), name='user-update'),  # Update user details
         path('users/<int:id>/delete/', UserDeleteView.as_view(), name='user-delete'),
     
]