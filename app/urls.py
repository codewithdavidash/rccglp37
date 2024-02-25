from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    LoginView,
)
from .views import *
from .forms import *

urlpatterns = [
    path('accounts/login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('settings/change-password-done/', PasswordChangeDoneView.as_view(
        template_name='app/changepassworddone.html'
        ), name='changepassworddone'),
    path('settings/profile/<str:pk>/', editprofile, name='editprofile'),
    path('update_record/<str:pk>/', update_record, name='update'),
    path('delete-record/<str:pk>/', delete_record, name='delete'),
    path('settings/change-password/', PasswordChangeView.as_view(
        template_name='app/changepassword.html',
        form_class=PasswordForm,
        success_url=reverse_lazy('changepassworddone')
    ), name='changepassword'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logoutView, name='logout'),
    path('my_records/', my_records, name='my_records'),
    path('detail/<str:pk>/', detail, name='detail'),
    path('settings/', settings, name='settings'),
    path('add-record/', add_record, name='add'),
    path('search/', search, name='search'),
    path('', index, name='index'),
]
