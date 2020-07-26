from django.conf import settings
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             next_url = request.GET.get('next') or 'profile'
#             return redirect('profile')
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

# signup = CreateView.as_view(model=User, 
#             form_class=SignupForm,
#             template_name='accounts/signup.html',
#             success_url=settings.LOGIN_URL)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
