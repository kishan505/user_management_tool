from django.urls import path
from .views import UserSignUpView, UserLoginView ,UserProfileView
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('sign_up', UserSignUpView.as_view()),
    path('login', UserLoginView.as_view()),
    path('create_user_profile', UserProfileView.as_view(), name="create_user_profile"),
]