from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return user.is_authenticated and user.role == 'admin'

def creator_required(user):
    return user.is_authenticated and user.role == 'creator'

def customer_required(user):
    return user.is_authenticated and user.role == 'customer'
