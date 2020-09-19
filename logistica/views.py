from django.shortcuts import render

def logistica(request):
    """para las paginas de logistica"""
    return render(request, 'logistica.html', {})
