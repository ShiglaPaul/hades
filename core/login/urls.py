from django.urls import path
from core.login.views import *
urlpatterns = [
    path('',LoginFormView.as_view(),name='login'),
    #path('logout/',LogoutView.as_view(),name='logout'),#sin next_page redirige a pagina por defecto de django o si declaras en setting, se redirige solo a login LOGOUT_REDIRECT_URL='/login/'
    path('logout/',LogoutRedirectView.as_view(),name='logout'),
]
