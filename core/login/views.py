from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import RedirectView
#admin@gmail.com 123
# Create your views here.
class LoginFormView(LoginView):
    template_name='login.html'
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Iniciar Sesion'
        return context

class LogoutRedirectView(RedirectView):
    pattern_name='login'
    def dispatch(self, request, *args,**kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)