# Mini Chatbot Inteligente — LóngBot 🐉

<p align="center">
  <strong>龍 LóngBot</strong> — Chatbot inteligente con red neuronal, inspirado en la filosofía china
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.2.12-green?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/scikit--learn-1.8.0-orange?logo=scikit-learn" alt="scikit-learn">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 📋 Descripción

**LóngBot** es un chatbot web inteligente construido con **Django** que utiliza una **red neuronal MLPClassifier** de scikit-learn para detectar intenciones del usuario mediante procesamiento de lenguaje natural (NLP). Su diseño visual está inspirado en la **filosofía china** con una paleta de colores elegante (jade, dorado, rojo imperial).

### ✨ Características

- 🧠 **Red neuronal MLP** con 2 capas ocultas (128/64 neuronas)
- 🎯 **16 intenciones** detectadas automáticamente
- 🔢 **Calculadora integrada** (suma, resta, multiplicación, división)
- 📊 **Vectorización TF-IDF** para procesamiento de texto
- 🏮 **Interfaz elegante** inspirada en filosofía china
- 📱 **Diseño responsivo** (móvil y escritorio)
- ✨ **Animaciones suaves** (partículas, burbujas, transiciones)
- 🔄 **Respuestas dinámicas** (hora y fecha en tiempo real)
- 🎋 **Citas filosóficas chinas** rotativas
- 📄 **Documentación IEEE/APA** en formato Word

---

## 🏗️ Arquitectura en Capas

El sistema sigue una **arquitectura modular de 4 capas**, donde cada nivel tiene una responsabilidad específica:

```
┌──────────────────────────────────────────────┐
│         🖥️  CAPA DE APLICACIÓN               │
│    Templates (HTML/CSS/JS) + Views + URLs    │
├──────────────────────────────────────────────┤
│         🧠  CAPA DE INTELIGENCIA             │
│    MLPClassifier (128→64→N) + LabelEncoder   │
├──────────────────────────────────────────────┤
│         ⚙️  CAPA DE PROCESAMIENTO            │
│    Normalización + Tokenización + TF-IDF     │
├──────────────────────────────────────────────┤
│         💾  CAPA DE DATOS                    │
│    Intenciones + Patrones + Respuestas       │
└──────────────────────────────────────────────┘
```

### Red Neuronal

| Capa | Neuronas | Activación |
|------|----------|------------|
| Entrada | TF-IDF (variable) | — |
| Oculta 1 | 128 | ReLU |
| Oculta 2 | 64 | ReLU |
| Salida | 16 (intenciones) | Softmax |

---

## 🗂️ Estructura del Proyecto

```
Mini-Chatbot/
├── manage.py
├── requirements.txt
├── README.md
├── chatbot_project/          # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── chatbot/                  # App principal
    ├── models.py             # Modelo Conversation
    ├── views.py              # Vistas + endpoint AJAX
    ├── urls.py               # Rutas
    ├── admin.py              # Panel de administración
    ├── apps.py               # Entrenamiento automático
    ├── tests.py              # Pruebas unitarias
    ├── engine/               # Motor NLP (4 capas)
    │   ├── data_layer.py         # Intenciones y respuestas
    │   ├── processing_layer.py   # Normalización + TF-IDF
    │   ├── intelligence_layer.py # Red neuronal MLP
    │   ├── response_layer.py     # Orquestador principal
    │   └── calculator.py         # Calculadora integrada
    ├── templates/chatbot/
    │   └── index.html        # Interfaz del chat
    └── static/chatbot/
        ├── css/style.css     # Estilos filosofía china
        └── js/chat.js        # Lógica de interacción
```

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Mini-Chatbot.git
cd Mini-Chatbot

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Ejecutar el servidor
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000/**

> La red neuronal se entrena automáticamente al iniciar el servidor.

---

## 🧪 Pruebas

```bash
python manage.py test chatbot
```

Las pruebas cubren:
- ✅ Normalización de texto (minúsculas, acentos, puntuación)
- ✅ Detección de intenciones (12 intenciones probadas)
- ✅ Vista AJAX (respuesta exitosa, vacía, método inválido)
- ✅ Respuestas por defecto

---

## 🎯 Intenciones Soportadas

| # | Intención | Ejemplo de entrada | Tipo de respuesta |
|---|---|---|---|
| 1 | Saludo | "hola", "buenos días" | Saludo con cita china |
| 2 | Despedida | "adiós", "bye" | Despedida filosófica |
| 3 | Hora | "qué hora es" | Hora actual del sistema |
| 4 | Fecha | "qué día es hoy" | Fecha actual formateada |
| 5 | IA | "qué es la IA" | Definición de IA |
| 6 | Nombre | "cómo te llamas" | Presentación del bot |
| 7 | Ayuda | "qué puedes hacer" | Menú de opciones |
| 8 | Chiste | "cuéntame un chiste" | Chiste aleatorio |
| 9 | Clima | "cómo está el clima" | Sugerencia con cita |
| 10 | Agradecimiento | "gracias" | Respuesta agradecida |
| 11 | Estado | "cómo estás" | Estado del bot |
| 12 | Filosofía | "dime de Confucio" | Cita filosófica china |
| 13 | Creador | "quién te creó" | Info del proyecto |
| 14 | Música | "recomienda música" | Recomendación musical |
| 15 | **Calculadora** | "5 + 3", "suma 10 y 20" | **Resultado de operación** |
| 16 | Matemáticas | "ecuación", "álgebra" | Info sobre matemáticas |

---

## 🎨 Diseño Visual

El diseño está inspirado en la **filosofía y estética china**:

- **Jade** (`#2d6a4f`) — Mensajes del bot
- **Rojo Imperial** (`#8B0000`) — Mensajes del usuario
- **Dorado** (`#d4a574`) — Títulos y acentos
- **Negro Tinta** (`#0a0a0f`) — Fondo principal

Elementos decorativos:
- Partículas flotantes (luciérnagas decorativas)
- Animaciones suaves de entrada
- Barra visual de la arquitectura de la red neuronal
- Citas filosóficas rotativas en el footer
- Caracteres chinos ornamentales (龍, 竹, ☯)

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| **Django 5.2.12** | Framework web backend |
| **scikit-learn 1.8.0** | Red neuronal MLPClassifier |
| **NumPy 2.4.2** | Cálculos matriciales |
| **Unidecode** | Normalización de acentos |
| **HTML/CSS/JS** | Frontend responsivo |
| **SQLite** | Base de datos (historial) |

---

## 📄 Licencia

Este proyecto fue desarrollado como actividad académica de **Sistemas Inteligentes**.

---

<p align="center">
  🐉 <em>«El viaje de mil millas comienza con un solo paso»</em> — Lao Tse
</p>
