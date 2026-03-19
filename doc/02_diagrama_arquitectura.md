# Diagrama de Arquitectura (Capas) — LóngBot

Este diagrama muestra la arquitectura en capas del sistema.

```mermaid
graph TB
    subgraph "CAPA DE PRESENTACIÓN"
        HTML["index.html<br/>Template Django"]
        CSS["style.css<br/>Estilos Filosofía China"]
        JS["chat.js<br/>Lógica Frontend"]
    end

    subgraph "CAPA DE APLICACIÓN"
        V["views.py<br/>Vistas Django"]
        URL["urls.py<br/>Enrutamiento"]
        MOD["models.py<br/>Modelo Conversation"]
    end

    subgraph "CAPA DE LÓGICA DE NEGOCIO"
        RL["response_layer.py<br/>Motor Principal (Singleton)"]
        CALC["calculator.py<br/>Procesador Matemático"]
    end

    subgraph "CAPA DE INTELIGENCIA"
        PL["processing_layer.py<br/>Normalización + TF-IDF"]
        IL["intelligence_layer.py<br/>Red Neuronal MLP"]
    end

    subgraph "CAPA DE DATOS"
        DL["data_layer.py<br/>Intenciones y Respuestas"]
        DB["db.sqlite3<br/>Base de Datos"]
    end

    HTML --> JS
    CSS --> HTML
    JS -->|"AJAX POST /send/"| V
    URL --> V
    V --> RL
    V --> MOD
    RL --> CALC
    RL --> PL
    RL --> IL
    RL --> DL
    IL --> PL
    MOD --> DB

    style HTML fill:#2d6a4f,color:#fff
    style CSS fill:#2d6a4f,color:#fff
    style JS fill:#2d6a4f,color:#fff
    style V fill:#d4a574,color:#000
    style URL fill:#d4a574,color:#000
    style MOD fill:#d4a574,color:#000
    style RL fill:#8B0000,color:#fff
    style CALC fill:#8B0000,color:#fff
    style PL fill:#1a1a2e,color:#fff
    style IL fill:#1a1a2e,color:#fff
    style DL fill:#0a0a0f,color:#d4a574
    style DB fill:#0a0a0f,color:#d4a574
```

## Responsabilidades por Capa

| Capa | Componente | Responsabilidad |
|---|---|---|
| Presentación | `index.html`, `style.css`, `chat.js` | Interfaz de usuario, interactividad, diseño visual |
| Aplicación | `views.py`, `urls.py`, `models.py` | Gestión HTTP, enrutamiento, persistencia |
| Lógica de Negocio | `response_layer.py`, `calculator.py` | Orquestación, detección de operaciones |
| Inteligencia | `processing_layer.py`, `intelligence_layer.py` | NLP, vectorización TF-IDF, red neuronal |
| Datos | `data_layer.py`, `db.sqlite3` | Base de conocimiento, almacenamiento |
