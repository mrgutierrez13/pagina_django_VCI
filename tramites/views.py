from django.shortcuts import render


def tramites(request):
    """para los tramites"""
    return render(request, 'tramites.html', {})


def sprocon_request(request):
    """Vista para mostrar sprocon"""
    return render(request, 'sprocon.html', {})

def ritex_request(request):
    """Vista para mostrar ritex"""
    return render(request, 'ritex.html', {})
