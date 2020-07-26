from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(reqeust):
    return render(reqeust, 'accounts/profile.html')
