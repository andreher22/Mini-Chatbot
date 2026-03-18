"""
Modelos de la aplicación Chatbot.

Define el modelo Conversation para almacenar el historial
de conversaciones en la base de datos (Capa de Datos).
"""

from django.db import models


class Conversation(models.Model):
    """
    Modelo que almacena cada intercambio de conversación:
    mensaje del usuario y respuesta del bot.
    """
    user_message = models.TextField(
        verbose_name="Mensaje del usuario"
    )
    bot_response = models.TextField(
        verbose_name="Respuesta del bot"
    )
    intent = models.CharField(
        max_length=50,
        verbose_name="Intención detectada",
        default="desconocida"
    )
    confidence = models.FloatField(
        verbose_name="Nivel de confianza",
        default=0.0
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Conversación"
        verbose_name_plural = "Conversaciones"

    def __str__(self):
        return f"[{self.intent}] {self.user_message[:50]}..."
