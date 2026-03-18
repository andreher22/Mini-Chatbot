"""
Pruebas unitarias del Chatbot.

Cubre:
- Normalización de texto (Capa de Procesamiento)
- Detección de intenciones (Capa de Inteligencia)
- Vista AJAX (Capa de Aplicación)
- Respuestas por defecto
"""

import json

from django.test import TestCase, Client


class TestProcesadorTexto(TestCase):
    """Pruebas de la capa de procesamiento."""

    def setUp(self):
        from chatbot.engine.processing_layer import ProcesadorTexto
        self.procesador = ProcesadorTexto()

    def test_normalizar_minusculas(self):
        resultado = self.procesador.normalizar("HOLA MUNDO")
        self.assertEqual(resultado, "hola mundo")

    def test_normalizar_acentos(self):
        resultado = self.procesador.normalizar("¿Cómo estás?")
        self.assertNotIn("ó", resultado)
        self.assertNotIn("á", resultado)

    def test_normalizar_puntuacion(self):
        resultado = self.procesador.normalizar("¡Hola! ¿Qué tal?")
        self.assertNotIn("!", resultado)
        self.assertNotIn("?", resultado)

    def test_normalizar_espacios(self):
        resultado = self.procesador.normalizar("  hola   mundo  ")
        self.assertEqual(resultado, "hola mundo")


class TestMotorChatbot(TestCase):
    """Pruebas de detección de intenciones (Motor completo)."""

    def setUp(self):
        from chatbot.engine.response_layer import MotorChatbot
        self.motor = MotorChatbot()
        self.motor.entrenar()

    def test_intencion_saludo(self):
        resultado = self.motor.procesar_mensaje("hola")
        self.assertEqual(resultado['intencion'], 'saludo')

    def test_intencion_despedida(self):
        resultado = self.motor.procesar_mensaje("adiós")
        self.assertEqual(resultado['intencion'], 'despedida')

    def test_intencion_hora(self):
        resultado = self.motor.procesar_mensaje("qué hora es")
        self.assertEqual(resultado['intencion'], 'hora')

    def test_intencion_fecha(self):
        resultado = self.motor.procesar_mensaje("qué día es hoy")
        self.assertEqual(resultado['intencion'], 'fecha')

    def test_intencion_ia(self):
        resultado = self.motor.procesar_mensaje("qué es la inteligencia artificial")
        self.assertEqual(resultado['intencion'], 'inteligencia_artificial')

    def test_intencion_nombre(self):
        resultado = self.motor.procesar_mensaje("cómo te llamas")
        self.assertEqual(resultado['intencion'], 'nombre')

    def test_intencion_ayuda(self):
        resultado = self.motor.procesar_mensaje("ayuda")
        self.assertEqual(resultado['intencion'], 'ayuda')

    def test_intencion_chiste(self):
        resultado = self.motor.procesar_mensaje("cuéntame un chiste")
        self.assertEqual(resultado['intencion'], 'chiste')

    def test_intencion_clima(self):
        resultado = self.motor.procesar_mensaje("cómo está el clima")
        self.assertEqual(resultado['intencion'], 'clima')

    def test_intencion_agradecimiento(self):
        resultado = self.motor.procesar_mensaje("muchas gracias")
        self.assertEqual(resultado['intencion'], 'agradecimiento')

    def test_intencion_estado(self):
        resultado = self.motor.procesar_mensaje("cómo estás")
        self.assertEqual(resultado['intencion'], 'estado')

    def test_intencion_filosofia(self):
        resultado = self.motor.procesar_mensaje("dime algo de confucio")
        self.assertEqual(resultado['intencion'], 'filosofia')

    def test_respuesta_contiene_texto(self):
        resultado = self.motor.procesar_mensaje("hola")
        self.assertTrue(len(resultado['respuesta']) > 0)

    def test_confianza_es_numero(self):
        resultado = self.motor.procesar_mensaje("hola")
        self.assertIsInstance(resultado['confianza'], float)
        self.assertGreaterEqual(resultado['confianza'], 0)
        self.assertLessEqual(resultado['confianza'], 1)


class TestVistaChat(TestCase):
    """Pruebas de la vista AJAX."""

    def setUp(self):
        self.client = Client()
        # Entrenar el motor
        from chatbot.engine.response_layer import motor
        motor.entrenar()

    def test_pagina_principal_carga(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LóngBot')

    def test_enviar_mensaje_exitoso(self):
        response = self.client.post(
            '/send/',
            data=json.dumps({'message': 'hola'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('response', data)
        self.assertIn('intent', data)
        self.assertIn('confidence', data)

    def test_enviar_mensaje_vacio(self):
        response = self.client.post(
            '/send/',
            data=json.dumps({'message': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_metodo_get_no_permitido(self):
        response = self.client.get('/send/')
        self.assertEqual(response.status_code, 405)

    def test_json_invalido(self):
        response = self.client.post(
            '/send/',
            data='not json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
