"""
Capa de Inteligencia - Red Neuronal (MLPClassifier).

Arquitectura de la red:
- Capa de entrada: Vector TF-IDF (dimensión variable)
- Capa oculta 1: 128 neuronas, activación ReLU
- Capa oculta 2: 64 neuronas, activación ReLU
- Capa de salida: N neuronas (una por intención), softmax

La red se entrena automáticamente al iniciar la aplicación
con los patrones definidos en data_layer.py.
"""

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder


class RedNeuronal:
    """
    Red neuronal MLP para detección de intenciones.
    Utiliza scikit-learn MLPClassifier con 2 capas ocultas.
    """

    def __init__(self):
        self.modelo = MLPClassifier(
            hidden_layer_sizes=(128, 64),  # 2 capas ocultas
            activation='relu',             # Función de activación
            solver='adam',                 # Optimizador Adam
            max_iter=1000,                 # Máximo de iteraciones
            random_state=42,               # Reproducibilidad
            early_stopping=False,          # Sin parada temprana (dataset pequeño)
            alpha=0.0001,                  # Regularización L2 baja
            learning_rate='adaptive',      # Learning rate adaptativo
            learning_rate_init=0.01,       # Learning rate inicial alto
            verbose=False
        )
        self.codificador = LabelEncoder()
        self._entrenado = False

    def entrenar(self, X, etiquetas: list[str]):
        """
        Entrena la red neuronal con los vectores TF-IDF y las etiquetas.

        Args:
            X: Matriz dispersa de vectores TF-IDF
            etiquetas: Lista de intenciones correspondientes
        """
        y = self.codificador.fit_transform(etiquetas)
        self.modelo.fit(X, y)
        self._entrenado = True

        # Información del entrenamiento
        n_capas = len(self.modelo.hidden_layer_sizes)
        n_intenciones = len(self.codificador.classes_)
        print(f"[LongBot] Red neuronal entrenada con exito:")
        print(f"   * Capas ocultas: {n_capas} ({self.modelo.hidden_layer_sizes})")
        print(f"   * Intenciones: {n_intenciones}")
        print(f"   * Iteraciones: {self.modelo.n_iter_}")
        print(f"   * Perdida final: {self.modelo.loss_:.4f}")

    def predecir(self, X) -> tuple[str, float]:
        """
        Predice la intención de un vector TF-IDF.

        Returns:
            tupla (intención, confianza)
        """
        if not self._entrenado:
            raise RuntimeError("La red neuronal no ha sido entrenada.")

        probabilidades = self.modelo.predict_proba(X)
        max_prob = np.max(probabilidades)
        prediccion_idx = np.argmax(probabilidades)
        intencion = self.codificador.inverse_transform([prediccion_idx])[0]

        return intencion, float(max_prob)

    def obtener_info_arquitectura(self) -> dict:
        """
        Retorna información sobre la arquitectura de la red.
        """
        if not self._entrenado:
            return {"estado": "no entrenada"}

        return {
            "capas_ocultas": list(self.modelo.hidden_layer_sizes),
            "activacion": self.modelo.activation,
            "optimizador": self.modelo.solver,
            "n_intenciones": len(self.codificador.classes_),
            "intenciones": list(self.codificador.classes_),
            "iteraciones": self.modelo.n_iter_,
            "perdida": round(self.modelo.loss_, 4)
        }
