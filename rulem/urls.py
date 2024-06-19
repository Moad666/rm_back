from django.urls import path
from .views import Register, Login, UserListAPIView,UserDeleteAPIView, RuleCreateAPIView,RuleListAPIView

urlpatterns = [
    # User
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    # Rules
    path('create_rule/', RuleCreateAPIView.as_view(), name='rule-create'),
    path('list_rule/', RuleListAPIView.as_view(), name='rule-list'),
]
