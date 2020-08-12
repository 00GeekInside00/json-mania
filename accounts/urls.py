from django.urls import path
from .views import SignUp
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('signup/', SignUp.as_view(

        form_class=SignUpForm), name='signup'),
]
