from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    release_settings = {
        'setting1': 'setting1',
        'setting2': 'setting2'
    }
    return JsonResponse(release_settings)
    
def release_settings(request):
    release_settings = [
        {"key": "ttt", "src": "text", "dest": "text", "status": True},
        {"key": "stt", "src": "speech", "dest": "text", "status": True},
        {"key": "sts", "src": "speech", "dest": "speech", "status": False},
        {"key": "tts", "src": "text", "dest": "speech", "status": True},
    ]
    
    return JsonResponse(release_settings, safe=False)
