"""
Vistas de la aplicación Chatbot (Capa de Aplicación).

Gestiona las peticiones HTTP:
- index: Renderiza la interfaz principal del chat
- send_message: Endpoint AJAX para procesar mensajes
- get_bot_info: Endpoint para información de la red neuronal
"""

import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from .engine.response_layer import motor


def index(request):
    """
    Vista principal: renderiza la interfaz del chatbot.
    """
    return render(request, 'chatbot/index.html')


@csrf_exempt
@require_POST
def send_message(request):
    """
    Endpoint AJAX para procesar mensajes del usuario.

    Recibe: JSON con campo 'message'
    Retorna: JSON con 'response', 'intent', 'confidence'
    """
    try:
        data = json.loads(request.body)
        mensaje = data.get('message', '').strip()

        if not mensaje:
            return JsonResponse({
                'error': 'El mensaje no puede estar vacío.',
                'response': '⚠️ Por favor, escribe un mensaje.',
                'intent': 'error',
                'confidence': 0
            }, status=400)

        # Procesar el mensaje con el motor del chatbot
        resultado = motor.procesar_mensaje(mensaje)

        # Guardar en la base de datos
        from .models import Conversation
        Conversation.objects.create(
            user_message=mensaje,
            bot_response=resultado['respuesta'],
            intent=resultado['intencion'],
            confidence=resultado['confianza']
        )

        return JsonResponse({
            'response': resultado['respuesta'],
            'intent': resultado['intencion'],
            'confidence': resultado['confianza']
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Formato JSON inválido.',
            'response': '⚠️ Error al procesar el mensaje.',
            'intent': 'error',
            'confidence': 0
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'response': '⚠️ Ocurrió un error interno. Intenta de nuevo.',
            'intent': 'error',
            'confidence': 0
        }, status=500)


@require_GET
def get_bot_info(request):
    """
    Endpoint para obtener información de la arquitectura de la red neuronal.
    """
    info = motor.obtener_info()
    return JsonResponse(info)
