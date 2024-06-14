from django.urls import path
from .views import Register, Login, UserListAPIView,UserDeleteAPIView

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    #path('delete_user/<int:pk>/', UserDeleteAPIView.as_view(), name='delete-user'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

]
