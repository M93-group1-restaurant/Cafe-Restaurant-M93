from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

@login_required
class CashierView(View):
    
    def get(self, request):
        ...
    
    def post(self, request):
        ...

@login_required
class ManagerView(View):

    def get(self, request):
        ...

