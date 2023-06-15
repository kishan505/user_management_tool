from django.urls import path
from .views import user_sign_up, user_login ,create_user_profile

urlpatterns = [
    path('sign_up', user_sign_up, name='sign_up'),
    path('login', user_login, name="login"),
    path('create_user_profile', create_user_profile, name="create_user_profile"),
]