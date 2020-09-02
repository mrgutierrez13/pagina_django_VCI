from django.shortcuts import render

# VISTAS


def asesora(request):
    """Vista para la seccion VCI te asesora"""
    context = {}
    # Render the HTML template
    return render(request, 'asesora.html', context=context)
