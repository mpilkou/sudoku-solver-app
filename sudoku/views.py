from django import template
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required

from oauth2_provider.decorators import protected_resource
from oauth2_provider.views.generic import ProtectedResourceView

# class ApiEndpoint(ProtectedResourceView):
#     pass

# Create your views here.
# @login_required
def index(req):
    return render(req, 'sudoku/index.html')

