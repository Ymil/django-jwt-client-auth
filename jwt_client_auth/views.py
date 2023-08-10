from . import JWT_ENDPOINT_ERROR_MESSAGE_FIELD, JWT_REDIRECT_URL, JWT_ENDPOINT, JWT_ENDPOINT_SSL_VERIFY
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .backends import JWTBackend
from .forms import LoginForm
import requests

User = get_user_model()


def login_by_jwt(username: str, password: str) -> str:
    payload = {"username": username, "password": password}
    response = requests.post(JWT_ENDPOINT, data=payload,
                             verify=JWT_ENDPOINT_SSL_VERIFY)
    if response.status_code == 200:
        token = response.json()['token']
        return token
    elif response.status_code == 403:
        raise Exception("Invalid credentials", response.json())
    else:
        raise Exception("Unknown error", response.json())


@login_required
def login_ok(request):
    return HttpResponse(f'<h1>Hi, {request.user.username}</h1><p>JWT: {request.session["jwt"]}</p>')


def login_view(request):
    if request.user.is_authenticated:
        return redirect(JWT_REDIRECT_URL) 

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            jwt = None
            try:
                jwt = login_by_jwt(username, password)
                username = username.lower()
                User.objects.get_or_create(username=username)
                user = JWTBackend().authenticate(request, username=username, password=password)
                login(request, user)
                request.session['jwt'] = jwt
                return redirect(JWT_REDIRECT_URL)
            except Exception as e:
                if(len(e.args) > 1 and JWT_ENDPOINT_ERROR_MESSAGE_FIELD in e.args[1]):
                    form.add_error(
                        None, e.args[1][JWT_ENDPOINT_ERROR_MESSAGE_FIELD]
                    )
                else:
                    raise e
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect(JWT_REDIRECT_URL)