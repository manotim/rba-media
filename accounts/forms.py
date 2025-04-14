# forms.py
from django import forms
from .models import AudioJournal, ImageUpload

class AudioJournalForm(forms.ModelForm):
    class Meta:
        model = AudioJournal
        fields = ['title', 'audio_file', 'category']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['title', 'image']
