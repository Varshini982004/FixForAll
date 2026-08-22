from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check passwords
        if password != confirm_password:
            return render(
                request,
                'users/register.html',
                {'error': 'Passwords do not match.'}
            )

        # Check username
        if User.objects.filter(username=username).exists():
            return render(
                request,
                'users/register.html',
                {'error': 'Username already exists.'}
            )

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Log the user in
        login(request, user)

        return redirect('/report/')

    return render(request, 'users/register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/report/')

        return render(
            request,
            'users/login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')