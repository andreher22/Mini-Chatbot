"""
Capa de Datos - Almacena las intenciones, patrones de entrada y respuestas.

Esta capa actúa como la base de conocimiento del chatbot, definiendo
qué intenciones puede detectar y cómo responder a cada una.
"""

import random
from datetime import datetime


# ============================================================
# Base de conocimiento: Intenciones, Patrones y Respuestas
# ============================================================

INTENCIONES = {
    "saludo": {
        "patrones": [
            "hola", "buenos dias", "buenas tardes", "buenas noches",
            "hey", "que tal", "saludos", "hi", "hello", "que onda",
            "como estas", "buen dia", "ey", "holi", "holaa"
        ],
        "respuestas": [
            "¡Hola! 🌸 Bienvenido al camino de la sabiduría. ¿En qué puedo ayudarte?",
            "¡Saludos, viajero! 🏮 Como dice Confucio: 'No importa lo lento que vayas, mientras no te detengas'. ¿Qué necesitas?",
            "¡Hola! 🎋 Es un placer recibirte. ¿Cómo puedo servirte hoy?",
            "¡Bienvenido! 🐉 El camino de mil pasos comienza con uno. ¿Cuál es tu pregunta?"
        ]
    },

    "despedida": {
        "patrones": [
            "adios", "bye", "hasta luego", "nos vemos", "chao",
            "hasta pronto", "me voy", "salir", "hasta manana",
            "que descanses", "goodbye", "ciao"
        ],
        "respuestas": [
            "¡Hasta pronto! 🌙 Que la paz del Tao te acompañe en tu camino.",
            "¡Adiós! 🎋 Recuerda: 'El viaje es la recompensa' — Confucio. ¡Vuelve cuando quieras!",
            "¡Nos vemos! 🏮 Que la armonía guíe tus pasos.",
            "¡Hasta luego! 🐉 Fue un placer hablar contigo. ¡Que tengas un excelente día!"
        ]
    },

    "hora": {
        "patrones": [
            "hora", "que hora es", "dime la hora", "hora actual",
            "que horas son", "tienes hora", "me dices la hora", "time"
        ],
        "respuestas": []  # Se generará dinámicamente
    },

    "fecha": {
        "patrones": [
            "fecha", "que dia es", "que dia es hoy", "hoy que dia es",
            "fecha actual", "dime la fecha", "que fecha es", "en que dia estamos"
        ],
        "respuestas": []  # Se generará dinámicamente
    },

    "inteligencia_artificial": {
        "patrones": [
            "inteligencia artificial", "ia", "que es ia", "que es la ia",
            "que es inteligencia artificial", "ai", "machine learning",
            "aprendizaje automatico", "redes neuronales", "deep learning"
        ],
        "respuestas": [
            "🧠 La Inteligencia Artificial es la simulación de procesos de inteligencia humana por parte de sistemas computacionales. Incluye aprendizaje, razonamiento y autocorrección. Como dijo Lao Tse: 'El sabio no compite, y por eso nadie puede competir con él'.",
            "🤖 La IA es una rama de la informática que busca crear máquinas capaces de realizar tareas que normalmente requieren inteligencia humana: reconocer patrones, tomar decisiones, comprender lenguaje natural y más.",
            "🧠 La Inteligencia Artificial combina algoritmos y datos para simular la capacidad humana de pensar y aprender. Yo mismo soy un ejemplo de IA aplicada al procesamiento de lenguaje natural."
        ]
    },

    "nombre": {
        "patrones": [
            "como te llamas", "tu nombre", "quien eres", "que eres",
            "presentate", "cual es tu nombre", "nombre del bot",
            "como te dicen", "dime tu nombre"
        ],
        "respuestas": [
            "🐉 Soy **LóngBot** (龙), un chatbot inteligente inspirado en la filosofía china. Mi nombre significa 'Dragón', símbolo de sabiduría y poder.",
            "🏮 Me llamo **LóngBot** (龙 — Dragón). Fui creado con Django y una red neuronal para entender tus mensajes y responder con sabiduría.",
            "🎋 ¡Soy LóngBot! Un asistente virtual que combina tecnología moderna con la antigua sabiduría china."
        ]
    },

    "ayuda": {
        "patrones": [
            "ayuda", "help", "que puedes hacer", "comandos", "opciones",
            "funciones", "que sabes hacer", "como funciones",
            "menu", "instrucciones"
        ],
        "respuestas": [
            "📜 **Puedo ayudarte con lo siguiente:**\n\n• 🕐 Decirte la **hora** actual\n• 📅 Decirte la **fecha** de hoy\n• 🧠 Explicarte sobre **Inteligencia Artificial**\n• 😄 Contarte un **chiste**\n• 🌤️ Hablarte del **clima**\n• 🎋 Compartir **filosofía china**\n• 🔢 **Calculadora**: suma, resta, multiplicación y división\n• 💬 Conversar contigo\n\nEscribe operaciones como: **5 + 3**, **suma 10 y 20**, **multiplica 4 por 7**"
        ]
    },

    "chiste": {
        "patrones": [
            "chiste", "cuentame algo gracioso", "humor", "algo gracioso",
            "hazme reir", "dime un chiste", "cuentame un chiste",
            "algo divertido", "broma"
        ],
        "respuestas": [
            "😄 ¿Por qué los programadores prefieren el modo oscuro? Porque la luz atrae bugs. 🐛",
            "😂 Un estudiante le dice al maestro: 'Maestro, ¿cómo logro la sabiduría?' Y el maestro responde: 'Leyendo la documentación antes de preguntar en Stack Overflow.'",
            "🤣 ¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
            "😆 ¿Qué le dijo un bit a otro? 'Nos vemos en el bus.'",
            "😄 Un programador va al supermercado. Su esposa le dice: 'Trae una botella de leche, y si hay huevos, trae seis.' Volvió con seis botellas de leche. 'Había huevos', explicó."
        ]
    },

    "clima": {
        "patrones": [
            "clima", "tiempo", "temperatura", "hace frio", "hace calor",
            "como esta el clima", "va a llover", "pronostico",
            "que tiempo hace", "lluvia"
        ],
        "respuestas": [
            "🌤️ Aunque no tengo acceso a datos meteorológicos en tiempo real, te sugiero consultar sitios como weather.com. Como dice el Tao: 'La naturaleza no se apresura, y sin embargo todo se logra'. 🍃",
            "☁️ No puedo ver el cielo desde aquí, pero recuerda la enseñanza china: 'Después de la tormenta siempre sale el sol'. 🌈 Te recomiendo revisar tu app del clima.",
            "🌧️ No tengo sensores de clima, pero como decía Lao Tse: 'El agua es la cosa más suave del mundo, pero puede atravesar la roca más dura'. Consulta un servicio meteorológico para datos precisos."
        ]
    },

    "agradecimiento": {
        "patrones": [
            "gracias", "thank you", "te agradezco", "muchas gracias",
            "mil gracias", "te lo agradezco", "genial gracias",
            "perfecto gracias", "thanks", "agradecido"
        ],
        "respuestas": [
            "🙏 ¡De nada! Como dice Confucio: 'La gratitud es la memoria del corazón'. Siempre es un placer ayudarte.",
            "🌸 ¡Con gusto! Estoy aquí para servirte. ¿Hay algo más en lo que pueda ayudarte?",
            "🏮 ¡No hay de qué! La verdadera riqueza es poder ayudar a los demás.",
            "🎋 ¡Es un placer! Recuerda que siempre puedes volver cuando necesites ayuda."
        ]
    },

    "estado": {
        "patrones": [
            "como estas", "que tal estas", "como te encuentras",
            "todo bien", "como andas", "como te va",
            "estas bien", "que tal te va"
        ],
        "respuestas": [
            "🐉 ¡Estoy en perfecta armonía! Funcionando al 100% y listo para ayudarte. ¿Tú cómo estás?",
            "🎋 ¡Muy bien, gracias por preguntar! Como el bambú, me mantengo flexible y firme. ¿En qué puedo servirte?",
            "🏮 ¡En equilibrio perfecto, como el yin y el yang! ¿Qué necesitas?"
        ]
    },

    "filosofia": {
        "patrones": [
            "confucio", "tao", "filosofia china", "lao tse", "lao tzu",
            "sabiduria", "proverbio", "proverbio chino", "cita",
            "ensenanza", "filosofia", "zen", "buda", "buddha",
            "sun tzu", "arte de la guerra", "i ching", "yin yang"
        ],
        "respuestas": [
            "🏮 **Confucio** dijo: *'No importa lo lento que vayas, siempre y cuando no te detengas.'* Esta enseñanza nos recuerda que la persistencia es más valiosa que la velocidad.",
            "🎋 **Lao Tse** enseñó: *'El viaje de mil millas comienza con un solo paso.'* Todo gran logro empieza con una pequeña acción.",
            "🐉 **Sun Tzu** escribió: *'La suprema excelencia consiste en romper la resistencia del enemigo sin luchar.'* La estrategia supera a la fuerza bruta.",
            "☯️ Del **Tao Te Ching**: *'El agua es fluida, suave y flexible. Pero el agua corroerá la roca, que es rígida y no se puede doblar.'* La adaptabilidad es poder.",
            "🌸 **Proverbio chino**: *'El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora.'*",
            "🏯 **Confucio** dijo: *'Estudia el pasado si quieres pronosticar el futuro.'* La historia es nuestra mejor maestra.",
            "☯️ **Yin y Yang**: Todo en el universo tiene dos fuerzas opuestas pero complementarias. La luz no existe sin la oscuridad, ni la alegría sin la tristeza."
        ]
    },

    "creador": {
        "patrones": [
            "quien te creo", "quien te hizo", "quien te programo",
            "de donde vienes", "quien es tu creador", "tu desarrollador"
        ],
        "respuestas": [
            "🛠️ Fui creado como un proyecto académico de **Sistemas Inteligentes**, construido con Django y una red neuronal MLPClassifier. ¡Soy producto de la unión entre tecnología y sabiduría! 🐉",
            "🏮 Nací de un proyecto universitario que combina **desarrollo web con Django** y **procesamiento de lenguaje natural**. ¡La tecnología aplicada a la educación!"
        ]
    },

    "musica": {
        "patrones": [
            "musica", "cancion", "canciones", "recomienda musica",
            "que musica", "playlist", "spotify"
        ],
        "respuestas": [
            "🎵 La música es el lenguaje universal del alma. Como decía Confucio: *'La música produce un tipo de placer que la naturaleza humana no puede prescindir.'* ¿Te gusta algún género en particular?",
            "🎶 Te recomiendo escuchar música tradicional china como el **guzheng** (cítara china) — es perfecta para relajarse y meditar. 🎋"
        ]
    },

    "calculadora": {
        "patrones": [
            "calculadora", "calcular", "calcula", "cuanto es", "cuanto da",
            "sumame", "restame", "multiplicame", "divideme",
            "operacion", "operaciones", "operacion matematica",
            "necesito calcular", "puedes calcular", "hacer cuentas",
            "sumar numeros", "restar numeros", "multiplicar numeros",
            "dividir numeros"
        ],
        "respuestas": [
            "🔢 ¡Soy tu calculadora!\n\nPuedes escribirme operaciones de varias formas:\n• **5 + 3** (con símbolos)\n• **suma 10 y 20** (con verbos)\n• **4 por 7** (con palabras)\n• **cuanto es 100 / 5** (preguntando)\n\nSoporto: **suma (+)**, **resta (-)**, **multiplicación (*)** y **división (/)**. ¡Prueba!",
            "🧮 ¡Puedo ayudarte con cálculos! Escríbeme la operación, por ejemplo:\n• **25 + 17**\n• **resta 50 y 15**\n• **8 por 6**\n• **divide 100 entre 4**\n\nComo decía Pitágoras: *‘Todo es número.’* ☯️"
        ]
    },

    "matematicas": {
        "patrones": [
            "matematicas", "ecuacion", "algebra", "geometria",
            "trigonometria", "derivada", "integral"
        ],
        "respuestas": [
            "🔢 Las matemáticas son el lenguaje del universo. Los antiguos chinos desarrollaron el ábaco hace más de 2000 años. ¡Puedo hacer cálculos básicos! Escribe algo como **5 + 3** o **multiplica 4 por 7**.",
            "📚 Como decía **Pitágoras**: ‘Todo es número.’ Puedo resolver sumas, restas, multiplicaciones y divisiones. ¡Prueba!"
        ]
    }
}

# ============================================================
# Respuesta por defecto (cuando no se detecta intención)
# ============================================================

RESPUESTAS_DEFAULT = [
    "🤔 Hmm, no estoy seguro de entender. ¿Podrías reformular tu pregunta? Escribe **'ayuda'** para ver qué puedo hacer.",
    "🎋 Interesante, pero no logro comprender del todo. Como decía Confucio: *'La ignorancia es la noche de la mente.'* ¿Podrías ser más específico?",
    "🐉 No estoy seguro de cómo responder a eso. Intenta preguntar sobre: hora, fecha, IA, chistes, filosofía o escribe **'ayuda'**.",
    "🏮 Perdona, aún estoy aprendiendo. ¿Podrías intentar con otras palabras?"
]


def obtener_respuesta_por_intencion(intencion: str) -> str:
    """
    Dada una intención detectada, retorna una respuesta apropiada.
    Para intenciones dinámicas (hora, fecha), genera la respuesta en tiempo real.
    """
    if intencion == "hora":
        ahora = datetime.now()
        hora_formateada = ahora.strftime("%I:%M %p")
        return f"🕐 La hora actual es **{hora_formateada}**. Como dice el proverbio chino: *'El tiempo es como un río — no puedes tocar la misma agua dos veces.'* ⏳"

    if intencion == "fecha":
        ahora = datetime.now()
        meses = [
            "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        dias_semana = [
            "lunes", "martes", "miércoles", "jueves",
            "viernes", "sábado", "domingo"
        ]
        dia_semana = dias_semana[ahora.weekday()]
        fecha = f"{dia_semana}, {ahora.day} de {meses[ahora.month]} de {ahora.year}"
        return f"📅 Hoy es **{fecha}**. Cada día es una nueva oportunidad. 🌅"

    if intencion in INTENCIONES and INTENCIONES[intencion]["respuestas"]:
        return random.choice(INTENCIONES[intencion]["respuestas"])

    return random.choice(RESPUESTAS_DEFAULT)


def obtener_respuesta_default() -> str:
    """Retorna una respuesta por defecto."""
    return random.choice(RESPUESTAS_DEFAULT)


def obtener_datos_entrenamiento():
    """
    Genera los datos de entrenamiento a partir de la base de conocimiento.
    Retorna una lista de tuplas (patrón, intención).
    """
    datos = []
    for intencion, contenido in INTENCIONES.items():
        for patron in contenido["patrones"]:
            datos.append((patron, intencion))
    return datos
