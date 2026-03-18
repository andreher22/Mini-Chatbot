"""
Capa de Respuesta - Toma de decisiones y generación de respuestas.

Coordina las capas inferiores para:
1. Recibir el mensaje del usuario
2. Procesarlo (normalización + vectorización)
3. Predecir la intención (red neuronal)
4. Generar la respuesta apropiada
"""

from .data_layer import (
    obtener_datos_entrenamiento,
    obtener_respuesta_por_intencion,
    obtener_respuesta_default,
)
from .processing_layer import ProcesadorTexto
from .intelligence_layer import RedNeuronal


# Umbral mínimo de confianza para aceptar una predicción
UMBRAL_CONFIANZA = 0.35


class MotorChatbot:
    """
    Motor principal del chatbot que integra todas las capas.
    Implementa el patrón Singleton para mantener una sola instancia.
    """

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self.procesador = ProcesadorTexto()
        self.red_neuronal = RedNeuronal()
        self._inicializado = True
        self._entrenado = False

    def entrenar(self):
        """
        Entrena el motor completo:
        1. Obtiene datos de entrenamiento de la capa de datos
        2. Aumenta los datos con variaciones (data augmentation)
        3. Entrena el vectorizador TF-IDF
        4. Entrena la red neuronal
        """
        if self._entrenado:
            return

        print("[LongBot] Iniciando entrenamiento del motor...")

        # Obtener datos de entrenamiento
        datos = obtener_datos_entrenamiento()

        # Data augmentation: generar variantes
        datos_aumentados = []
        prefijos = ["", "oye ", "dime ", "me puedes decir ", "quiero saber "]
        for texto, intencion in datos:
            datos_aumentados.append((texto, intencion))
            for prefijo in prefijos[1:]:  # Saltar el vacío
                datos_aumentados.append((prefijo + texto, intencion))

        textos = [d[0] for d in datos_aumentados]
        etiquetas = [d[1] for d in datos_aumentados]

        print(f"[LongBot] Datos cargados: {len(datos)} patrones originales, "
              f"{len(textos)} con augmentation, "
              f"{len(set(etiquetas))} intenciones")

        # Entrenar vectorizador (Capa de Procesamiento)
        self.procesador.entrenar_vectorizador(textos)

        # Vectorizar textos
        X = self.procesador.vectorizar(textos)

        # Entrenar red neuronal (Capa de Inteligencia)
        self.red_neuronal.entrenar(X, etiquetas)

        self._entrenado = True
        print("[LongBot] Motor listo para recibir mensajes.")

    def procesar_mensaje(self, mensaje: str) -> dict:
        """
        Procesa un mensaje del usuario y genera una respuesta.

        Args:
            mensaje: Texto escrito por el usuario

        Returns:
            dict con: respuesta, intencion, confianza
        """
        if not self._entrenado:
            self.entrenar()

        # Vectorizar el mensaje del usuario
        X = self.procesador.vectorizar_uno(mensaje)

        # Predecir intención
        intencion, confianza = self.red_neuronal.predecir(X)

        # Decidir respuesta según confianza
        if confianza >= UMBRAL_CONFIANZA:
            respuesta = obtener_respuesta_por_intencion(intencion)
        else:
            respuesta = obtener_respuesta_default()
            intencion = "desconocida"

        return {
            "respuesta": respuesta,
            "intencion": intencion,
            "confianza": round(confianza, 4)
        }

    def obtener_info(self) -> dict:
        """Retorna información del motor para depuración."""
        return self.red_neuronal.obtener_info_arquitectura()


# Instancia global del motor
motor = MotorChatbot()
