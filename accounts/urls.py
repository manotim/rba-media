from django.urls import path
from .views import register, user_login, user_logout, admin_dashboard, creator_dashboard, customer_dashboard, upload_audio, upload_image, purchase_audio, purchase_image

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('creator-dashboard/', creator_dashboard, name='creator_dashboard'),
    path('customer-dashboard/', customer_dashboard, name='customer_dashboard'),
    path('upload-audio/', upload_audio, name='upload_audio'),
    path('upload-image/', upload_image, name='upload_image'),
    # 🔥 Add these two lines:
    path('purchase/audio/<int:audio_id>/', purchase_audio, name='purchase_audio'),
    path('purchase/image/<int:image_id>/', purchase_image, name='purchase_image'),
]
