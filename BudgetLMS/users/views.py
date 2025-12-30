from django.shortcuts import redirect, render
from django.contrib.auth import logout as user_logout

# Create your views here.
def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    user_logout(request)
    return redirect('dashboard')

