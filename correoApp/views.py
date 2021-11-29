from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

from rest_framework import status, generics

# Create your views here.

class correoApp(generics.CreateAPIView):


    def send_email(correo1, correo2):
    
        context = {'mail':mail, 'usuario':correo1, 'predio':correo1, 'predio_id':correo1}

        template = get_template('correo.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Solicitud Hoja de Vida',
            '',
            correo1,
            [correo2],
        )
        print(settings.EMAIL_HOST_USER)

        email.attach_alternative(content, 'text/html')
        email.send()

        """def send_email(compra, predio_id):
        usuario = compra.usuario
        predio = compra.predio
        #usuario2 = Usuario2.objects.get(email=mail)
        context = {'mail':mail, 'usuario':usuario, 'predio':predio, 'predio_id':predio_id}

        template = get_template('correo.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Compensave - Huella de Carbono',
            '',
            settings.EMAIL_HOST_USER,
            [usuario.email],
        )
        print(settings.EMAIL_HOST_USER)

        email.attach_alternative(content, 'text/html')
        email.send()"""