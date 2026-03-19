"""
Módulo de Calculadora - Procesamiento de operaciones matemáticas.

Detecta y resuelve operaciones aritméticas básicas:
- Suma (+, más, sumar)
- Resta (-, menos, restar)
- Multiplicación (*, por, multiplicar)
- División (/, entre, dividir)

Soporta formatos como:
- "cuanto es 5 + 3"
- "suma 10 y 20"
- "multiplica 4 por 7"
- "5 mas 3"
- "resta 15 menos 8"
- "divide 100 entre 5"
"""

import re


# Mapeo de palabras a operadores
OPERADORES_TEXTO = {
    'mas': '+', 'sumar': '+', 'suma': '+', 'sumale': '+', 'agregar': '+',
    'menos': '-', 'restar': '-', 'resta': '-', 'restale': '-', 'quitar': '-',
    'por': '*', 'multiplicar': '*', 'multiplica': '*', 'multiplicado': '*',
    'entre': '/', 'dividir': '/', 'divide': '/', 'dividido': '/',
}


def detectar_operacion(texto: str) -> dict | None:
    """
    Detecta si el texto contiene una operación matemática y la resuelve.

    Args:
        texto: Mensaje del usuario (ya normalizado, sin acentos).

    Returns:
        dict con resultado, operacion, num1, num2 si encuentra operación.
        None si no encuentra una operación válida.
    """
    texto = texto.lower().strip()

    # Patrón 1: "5 + 3", "10 - 2", "4 * 7", "100 / 5"
    patron_simbolos = re.search(
        r'(-?\d+(?:\.\d+)?)\s*([+\-*/x])\s*(-?\d+(?:\.\d+)?)',
        texto
    )
    if patron_simbolos:
        num1 = float(patron_simbolos.group(1))
        operador = patron_simbolos.group(2)
        num2 = float(patron_simbolos.group(3))
        if operador == 'x':
            operador = '*'
        return _ejecutar_operacion(num1, operador, num2)

    # Patrón 2: "suma 5 y 3", "resta 10 y 2", "multiplica 4 y 7"
    patron_verbo_y = re.search(
        r'(suma|resta|multiplica|divide|sumar|restar|multiplicar|dividir)\s+(-?\d+(?:\.\d+)?)\s+(?:y|con)\s+(-?\d+(?:\.\d+)?)',
        texto
    )
    if patron_verbo_y:
        operador = OPERADORES_TEXTO.get(patron_verbo_y.group(1), '+')
        num1 = float(patron_verbo_y.group(2))
        num2 = float(patron_verbo_y.group(3))
        return _ejecutar_operacion(num1, operador, num2)

    # Patrón 3: "5 mas 3", "10 menos 2", "4 por 7", "100 entre 5"
    patron_texto = re.search(
        r'(-?\d+(?:\.\d+)?)\s+(mas|menos|por|entre|multiplicado|dividido|sumado|restado)\s+(-?\d+(?:\.\d+)?)',
        texto
    )
    if patron_texto:
        num1 = float(patron_texto.group(1))
        palabra = patron_texto.group(2)
        num2 = float(patron_texto.group(3))
        operador = OPERADORES_TEXTO.get(palabra, '+')
        return _ejecutar_operacion(num1, operador, num2)

    # Patrón 4: "cuanto es 5 + 3" o "calcula 10 - 2"
    patron_cuanto = re.search(
        r'(?:cuanto\s+es|calcula|resuelve|resultado\s+de)\s+(-?\d+(?:\.\d+)?)\s*([+\-*/x])\s*(-?\d+(?:\.\d+)?)',
        texto
    )
    if patron_cuanto:
        num1 = float(patron_cuanto.group(1))
        operador = patron_cuanto.group(2)
        num2 = float(patron_cuanto.group(3))
        if operador == 'x':
            operador = '*'
        return _ejecutar_operacion(num1, operador, num2)

    # Patrón 5: "sumale 5 a 3", "restale 2 a 10"
    patron_le_a = re.search(
        r'(sumale|restale|agregale|quitale)\s+(-?\d+(?:\.\d+)?)\s+a\s+(-?\d+(?:\.\d+)?)',
        texto
    )
    if patron_le_a:
        palabra = patron_le_a.group(1)
        num1 = float(patron_le_a.group(3))  # "a 10" es la base
        num2 = float(patron_le_a.group(2))  # "sumale 5" es la cantidad
        operador = OPERADORES_TEXTO.get(palabra, '+')
        return _ejecutar_operacion(num1, operador, num2)

    return None


def _ejecutar_operacion(num1: float, operador: str, num2: float) -> dict:
    """
    Ejecuta una operación matemática y retorna el resultado formateado.
    """
    nombre_ops = {
        '+': 'suma', '-': 'resta',
        '*': 'multiplicacion', '/': 'division'
    }
    simbolos_display = {
        '+': '+', '-': '-',
        '*': '×', '/': '÷'
    }

    try:
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                return {
                    'exito': False,
                    'operacion': 'division',
                    'error': 'division_por_cero',
                    'respuesta': _formatear_error_division()
                }
            resultado = num1 / num2
        else:
            return None

        # Formatear número (sin decimales si es entero)
        if resultado == int(resultado):
            resultado_str = str(int(resultado))
        else:
            resultado_str = f"{resultado:.4f}".rstrip('0').rstrip('.')

        # Formatear numeros de entrada
        n1_str = str(int(num1)) if num1 == int(num1) else str(num1)
        n2_str = str(int(num2)) if num2 == int(num2) else str(num2)

        simbolo = simbolos_display.get(operador, operador)
        nombre = nombre_ops.get(operador, 'operacion')

        return {
            'exito': True,
            'operacion': nombre,
            'num1': num1,
            'num2': num2,
            'resultado': resultado,
            'respuesta': _formatear_respuesta(n1_str, simbolo, n2_str, resultado_str, nombre)
        }

    except Exception:
        return None


def _formatear_respuesta(n1: str, simbolo: str, n2: str, resultado: str, nombre: str) -> str:
    """Genera una respuesta elegante con la operación resuelta."""
    import random
    plantillas = [
        f"🔢 **{nombre.capitalize()}:**\n\n`{n1} {simbolo} {n2} = **{resultado}**`\n\nComo decía el antiguo proverbio chino: *'Los números no mienten.'* 🏮",
        f"🧮 ¡Calculado!\n\n`{n1} {simbolo} {n2} = **{resultado}**`\n\nLos chinos inventaron el ábaco hace más de 2000 años. ¡La sabiduría numérica perdura! 🐉",
        f"📐 El resultado de **{n1} {simbolo} {n2}** es: **{resultado}**\n\nComo dijo Pitágoras: *'Todo es número.'* ☯️",
    ]
    return random.choice(plantillas)


def _formatear_error_division() -> str:
    """Respuesta para división entre cero."""
    import random
    errores = [
        "⚠️ ¡No es posible dividir entre cero! Como dice el Tao: *'De la nada no puede surgir algo.'* ☯️",
        "🚫 La división entre cero no está definida. Como enseña Confucio: *'El que sabe que no sabe, ese es el verdadero sabio.'* 🏮",
    ]
    return random.choice(errores)


def es_operacion_matematica(texto: str) -> bool:
    """
    Verifica rápidamente si un texto podría contener una operación matemática.
    """
    texto = texto.lower()
    # Buscar patrones numéricos con operadores
    if re.search(r'\d+\s*[+\-*/x]\s*\d+', texto):
        return True
    # Buscar palabras clave de operaciones con números
    palabras_op = ['suma', 'resta', 'multiplica', 'divide', 'sumar', 'restar',
                   'multiplicar', 'dividir', 'cuanto es', 'calcula', 'resuelve',
                   'sumale', 'restale']
    if any(p in texto for p in palabras_op) and re.search(r'\d', texto):
        return True
    # Buscar "N mas/menos/por/entre N"
    if re.search(r'\d+\s+(mas|menos|por|entre)\s+\d+', texto):
        return True
    return False
