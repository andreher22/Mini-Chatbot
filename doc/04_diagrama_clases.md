# Diagrama de Clases — LóngBot

Modelo de clases del sistema con relaciones y métodos principales.

```mermaid
classDiagram
    class MotorChatbot {
        -_instancia: MotorChatbot
        -_inicializado: bool
        -_entrenado: bool
        +procesador: ProcesadorTexto
        +red_neuronal: RedNeuronal
        +__new__() MotorChatbot
        +__init__()
        +entrenar()
        +procesar_mensaje(mensaje: str) dict
        +obtener_info() dict
    }

    class ProcesadorTexto {
        +vectorizador: TfidfVectorizer
        +normalizar(texto: str) str
        +entrenar_vectorizador(textos: list)
        +vectorizar(textos: list) matrix
        +vectorizar_uno(texto: str) matrix
    }

    class RedNeuronal {
        +modelo: MLPClassifier
        +codificador: LabelEncoder
        -_entrenado: bool
        +entrenar(X, etiquetas: list)
        +predecir(X) tuple
        +obtener_info_arquitectura() dict
    }

    class Calculator {
        +detectar_operacion(texto: str) dict
        +es_operacion_matematica(texto: str) bool
        -_ejecutar_operacion(n1, op, n2) dict
        -_formatear_respuesta() str
        -_formatear_error_division() str
    }

    class DataLayer {
        +INTENCIONES: dict
        +RESPUESTAS_DEFAULT: list
        +obtener_respuesta_por_intencion(intent: str) str
        +obtener_respuesta_default() str
        +obtener_datos_entrenamiento() list
    }

    class Conversation {
        +user_message: str
        +bot_response: str
        +intent: str
        +confidence: float
        +created_at: datetime
        +__str__() str
    }

    class MLPClassifier {
        +hidden_layer_sizes: tuple
        +activation: str
        +solver: str
        +fit(X, y)
        +predict_proba(X) array
    }

    class TfidfVectorizer {
        +max_features: int
        +ngram_range: tuple
        +fit(textos)
        +transform(textos) matrix
    }

    MotorChatbot --> ProcesadorTexto : usa
    MotorChatbot --> RedNeuronal : usa
    MotorChatbot --> Calculator : usa
    MotorChatbot --> DataLayer : consulta
    RedNeuronal --> MLPClassifier : contiene
    RedNeuronal --> LabelEncoder : contiene
    ProcesadorTexto --> TfidfVectorizer : contiene
    Conversation ..> MotorChatbot : "se genera desde"

    class LabelEncoder {
        +classes_: array
        +fit_transform(y) array
        +inverse_transform(y) array
    }
```

## Patrones de Diseño Utilizados

| Patrón | Clase | Descripción |
|---|---|---|
| **Singleton** | `MotorChatbot` | Una sola instancia del motor en toda la aplicación |
| **Layered Architecture** | Todo el sistema | Separación en capas de datos, procesamiento, inteligencia y aplicación |
| **Strategy** | `Calculator` / `RedNeuronal` | Diferentes estrategias de procesamiento según el tipo de entrada |
| **MVC** | `views.py` / `models.py` / `templates/` | Modelo-Vista-Controlador de Django |
