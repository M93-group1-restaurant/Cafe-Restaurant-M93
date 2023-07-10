from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View


class CashierView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    def get(self, request):
        ...
    
    def post(self, request):
        ...


class ManagerView(LoginRequiredMixin, PermissionRequiredMixin, View):

    def get(self, request):
        ...

