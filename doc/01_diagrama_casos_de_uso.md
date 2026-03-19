# Diagrama de Casos de Uso — LóngBot

Este diagrama muestra las interacciones principales entre el usuario y el sistema.

```mermaid
graph LR
    subgraph "Actores"
        U["👤 Usuario"]
        A["👨‍💼 Admin"]
    end

    subgraph "LóngBot - Sistema Chatbot"
        UC1["Enviar mensaje"]
        UC2["Recibir respuesta"]
        UC3["Consultar hora/fecha"]
        UC4["Pedir chiste"]
        UC5["Preguntar sobre IA"]
        UC6["Usar calculadora"]
        UC7["Consultar filosofía"]
        UC8["Pedir ayuda"]
        UC9["Ver historial (Admin)"]
    end

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC6
    U --> UC7
    U --> UC8
    A --> UC9

    UC1 --> UC2
```

## Descripción de Casos de Uso

| Caso de Uso | Actor | Descripción |
|---|---|---|
| Enviar mensaje | Usuario | El usuario escribe un mensaje en la interfaz del chat |
| Recibir respuesta | Usuario | El sistema responde con la intención detectada |
| Consultar hora/fecha | Usuario | Obtener la hora o fecha actual |
| Pedir chiste | Usuario | Solicitar contenido humorístico |
| Preguntar sobre IA | Usuario | Consultar sobre inteligencia artificial |
| Usar calculadora | Usuario | Realizar operaciones matemáticas (+, -, *, /) |
| Consultar filosofía | Usuario | Obtener citas y enseñanzas chinas |
| Pedir ayuda | Usuario | Ver el menú de funcionalidades |
| Ver historial | Admin | Consultar conversaciones previas (Django Admin) |
