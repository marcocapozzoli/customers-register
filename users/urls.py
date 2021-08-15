from django.urls import path
from . import views


urlpatterns = [
    
    # Forget Password
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    path('', views.dash, name='dash'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('logout', views.CustomLogoutView.as_view(), name='logout'),
]