from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('StrorageList')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/registration.html', {'form': form})


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('StrorageList')
