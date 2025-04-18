from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from .models import CustomUser, AudioJournal, ImageUpload
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .decorators import admin_required, creator_required, customer_required
from .forms import AudioJournalForm, ImageUploadForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = CustomUser.objects.create_user(username=username, password=password, role=role)

        # Assign user to the appropriate group
        group = Group.objects.get(name=role.capitalize())
        user.groups.add(group)
        user.save()

        return redirect('login')

    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            # Redirect based on role
            if user.groups.filter(name="Admin").exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Creator').exists():
                return redirect('creator_dashboard')
            elif user.groups.filter(name="Customer").exists():
                return redirect('customer_dashboard')

        return redirect('login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@user_passes_test(admin_required)
@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@user_passes_test(creator_required)
@login_required
def creator_dashboard(request):
    audio_form = AudioJournalForm()
    image_form = ImageUploadForm()
    uploaded_audios = AudioJournal.objects.filter(creator=request.user)
    uploaded_images = ImageUpload.objects.filter(creator=request.user)

    return render(request, 'accounts/creator_dashboard.html', {
        'audio_form': audio_form,
        'image_form': image_form,
        'uploaded_audios': uploaded_audios,
        'uploaded_images': uploaded_images,
    })

@user_passes_test(customer_required)
@login_required
def customer_dashboard(request):
    # Fetching Gospel and Secular audio journals
    gospel_audios = AudioJournal.objects.filter(category='gospel')
    secular_audios = AudioJournal.objects.filter(category='secular')
    
    # Fetching all uploaded images
    all_images = ImageUpload.objects.all()

    return render(request, 'accounts/customer_dashboard.html', {
        'gospel_audios': gospel_audios,
        'secular_audios': secular_audios,
        'all_images': all_images,
    })




@user_passes_test(creator_required)
@login_required
def upload_audio(request):
    messages.success(request, 'Audio uploaded successfully!')
    if request.method == 'POST':
        form = AudioJournalForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.creator = request.user
            audio.save()
            return redirect('creator_dashboard')
    else:
        form = AudioJournalForm()
    return render(request, 'accounts/upload_audio.html', {'form': form})

@user_passes_test(creator_required)
@login_required
def upload_image(request):
    messages.success(request, 'Image uploaded successfully!')
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.creator = request.user
            image.save()
            return redirect('creator_dashboard')
    else:
        form = ImageUploadForm()
    return render(request, 'accounts/upload_image.html', {'form': form})
