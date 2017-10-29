from django.shortcuts import render
from django.views import View

from .forms import LoginForm

# Create your views here.
class LoginFormView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})