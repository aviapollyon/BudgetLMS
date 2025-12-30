from django.shortcuts import render

# Create your views here.
def DashboardView(request):
    return render(request, 'LMS/Dashboard.html')