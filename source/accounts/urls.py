from accounts.views import login_view, logout_view
from django.urls import path

urlpatterns = [
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),

]