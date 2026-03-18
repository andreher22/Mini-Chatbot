"""
Configuración de la app Chatbot.
El motor del chatbot se entrena automáticamente al iniciar.
"""

from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    verbose_name = 'LóngBot - Chatbot Inteligente'

    def ready(self):
        """
        Se ejecuta al iniciar la aplicación.
        Entrena la red neuronal con los datos de la capa de datos.
        """
        import sys
        # Solo entrenar cuando se ejecuta el servidor, no en migraciones
        if 'runserver' in sys.argv or 'test' in sys.argv:
            from .engine.response_layer import motor
            motor.entrenar()
