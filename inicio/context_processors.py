from inicio.models import RedSocial, RedSocialEnlace


def base_request(request):
    """Para pasar datos a todas las plantillas del proyecto"""
    redes = RedSocial.objects.all()
    redes_enlaces = RedSocialEnlace.objects.all()
    # Render the HTML template
    return {
        'redes': redes,
        'redes_enlaces': redes_enlaces,
    }
