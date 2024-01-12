from django.contrib.auth import get_user_model, authenticate, login, logout

from django.shortcuts import render, redirect


User = get_user_model()

from . forms import RegisterForm, LoginForm



def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        try:
            user = User.objects.create_user(username, email, password1)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['Register_errors'] = 1
    return render(request, 'accounts/register.html', {
        'form': form
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')

        user = authenticate(request, username=username, password=password1)

        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['Login_errors'] = 1
    return render(request, 'accounts/login.html', {
        'form': form
    })