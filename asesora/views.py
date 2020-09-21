from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from asesora.forms import ContactoForm, ResponderForm


def asesora(request):
    """Para manejar los datos del formulario VCI te Asesora"""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('gracias/')
    else:
        form = ContactoForm()

    return render(request, 'asesora.html', {'formulario': form})


def asesora_gracias(request):
    """Cuando los datos del VCI asesora fue exitoso"""
    return render(request, 'asesora_gracias.html', {})


def responder_email(request):
    """Para responder un correo individual"""
    if request.method == 'GET':
        form = ResponderForm()
    else:
        form = ResponderForm(request.POST)
        if form.is_valid():
            acerca = form.cleaned_data['acerca']
            email_emisor = form.cleaned_data['email_emisor']
            email_receptor = form.cleaned_data['email_receptor']
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(acerca, mensaje, email_emisor, email_receptor)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "responder.html", {'form': form})
