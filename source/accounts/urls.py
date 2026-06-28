from accounts.views import logout_view, RegisterView, AuthLoginView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('accounts/login/', AuthLoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]