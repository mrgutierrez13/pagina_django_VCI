from django.shortcuts import render


def en_desarrollo(request):
    """Placeholder para paginas en desarrollo"""
    return render(request, 'en_desarrollo.html', {})
