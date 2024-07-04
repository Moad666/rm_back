from django.urls import path
from .views import *

urlpatterns = [
    # User
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    # Rules
    path('create_rule/', RuleCreateAPIView.as_view(), name='rule-create'),
    path('list_rule/', RuleListAPIView.as_view(), name='rule-list'),
    path('update_rule/<int:pk>', RuleUpdateAPIView.as_view(), name='rule-update'),
    path('delete_rule/<int:pk>', RuleDeleteAPIView.as_view(), name='rule-delete'),

    # Categorie
    path('create_categorie/', CategorieCreateAPIView.as_view(), name='categorie-create'),
    path('delete_categorie/<int:pk>', CategorieDeleteAPIView.as_view(), name='categorie-delete'),
]
