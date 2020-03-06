from django.conf.urls import url
from django.urls import path, reverse_lazy, re_path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [ 
    path('', PasswordResetView.as_view(template_name='reset_password/password_reset_form.html'),
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/', PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'),
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'), name='password_reset_complete'),  
]