from django.urls import path
from .views import register, user_login, user_logout, admin_dashboard, creator_dashboard, customer_dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('creator-dashboard/', creator_dashboard, name='creator_dashboard'),
    path('customer-dashboard/', customer_dashboard, name='customer_dashboard'),
]
