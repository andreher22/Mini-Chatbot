"""
Capa de Procesamiento - Transforma el texto crudo en información útil.

Funciones principales:
- Normalización de texto (minúsculas, sin acentos, sin puntuación)
- Tokenización
- Vectorización TF-IDF para alimentar la red neuronal
"""

import re
import string

from unidecode import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer


class ProcesadorTexto:
    """
    Procesa y normaliza el texto del usuario para prepararlo
    para la capa de inteligencia.
    """

    def __init__(self):
        self.vectorizador = TfidfVectorizer(
            max_features=500,
            ngram_range=(1, 2),  # Unigramas y bigramas
            sublinear_tf=True
        )
        self._entrenado = False

    def normalizar(self, texto: str) -> str:
        """
        Normaliza el texto:
        1. Convierte a minúsculas
        2. Elimina acentos
        3. Elimina signos de puntuación
        4. Elimina espacios extra
        """
        texto = texto.lower().strip()
        texto = unidecode(texto)
        texto = re.sub(f"[{re.escape(string.punctuation)}]", " ", texto)
        texto = re.sub(r"\s+", " ", texto).strip()
        return texto

    def entrenar_vectorizador(self, textos: list[str]):
        """
        Entrena el vectorizador TF-IDF con los textos de entrenamiento.
        """
        textos_normalizados = [self.normalizar(t) for t in textos]
        self.vectorizador.fit(textos_normalizados)
        self._entrenado = True

    def vectorizar(self, textos: list[str]):
        """
        Transforma textos en vectores TF-IDF.
        El vectorizador debe estar entrenado previamente.
        """
        if not self._entrenado:
            raise RuntimeError("El vectorizador no ha sido entrenado.")
        textos_normalizados = [self.normalizar(t) for t in textos]
        return self.vectorizador.transform(textos_normalizados)

    def vectorizar_uno(self, texto: str):
        """
        Vectoriza un solo texto (para predicción individual).
        """
        return self.vectorizar([texto])
