from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from .models import CustomUser
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .decorators import admin_required, creator_required, customer_required


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = CustomUser.objects.create_user(username=username, password=password, role=role)

        # Assign user to the appropriate group
        group = Group.objects.get(name=role.capitalize())
        user.groups.add(group)
        user.save()

        return redirect('login')

    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            # Redirect based on role
            if user.groups.filter(name="Admin").exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Creator').exists():
                return redirect('creator_dashboard')
            elif user.groups.filter(name="Customer").exists():
                return redirect('customer_dashboard')

        return redirect('login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@user_passes_test(admin_required)
@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@user_passes_test(creator_required)
@login_required
def creator_dashboard(request):
    return render(request, 'accounts/creator_dashboard.html')

@user_passes_test(customer_required)
@login_required
def customer_dashboard(request):
    return render(request, 'accounts/customer_dashboard.html')
