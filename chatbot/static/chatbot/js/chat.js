/**
 * LóngBot — Lógica de Interacción del Chat
 * Maneja el envío de mensajes, animaciones y partículas de fondo.
 */

// ============================================================
// Inicialización
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initKeyboardEvents();
    rotateFooterQuotes();
});

// ============================================================
// Configuración
// ============================================================

const SEND_URL = '/send/';
const QUOTES = [
    '«El viaje de mil millas comienza con un solo paso» — Lao Tse',
    '«No importa lo lento que vayas, mientras no te detengas» — Confucio',
    '«La mejor hora para plantar un árbol fue hace 20 años. La segunda, ahora» — Proverbio chino',
    '«Estudia el pasado si quieres pronosticar el futuro» — Confucio',
    '«El agua vence a la piedra, no por la fuerza sino por la persistencia» — Proverbio chino',
    '«Aquel que conoce a los demás es sabio; el que se conoce a sí mismo es iluminado» — Lao Tse',
    '«La paciencia es un árbol de raíz amarga pero de frutos muy dulces» — Proverbio chino',
];

// ============================================================
// Enviar mensaje
// ============================================================

async function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    if (!message) return;

    // Limpiar input
    input.value = '';
    input.focus();

    // Ocultar bienvenida
    hideWelcome();

    // Mostrar mensaje del usuario
    addUserBubble(message);

    // Mostrar indicador de escritura
    showTypingIndicator();

    // Activar animación de capas de la red neuronal
    animateNNLayers();

    try {
        const response = await fetch(SEND_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Quitar indicador de escritura
        removeTypingIndicator();

        // Mostrar respuesta del bot
        addBotBubble(data.response);

        // Actualizar barra de intención
        updateIntentBar(data.intent, data.confidence);

    } catch (error) {
        removeTypingIndicator();
        addBotBubble('⚠️ Error de conexión. Por favor, intenta de nuevo.');
        console.error('Error:', error);
    }
}

function sendQuickMessage(msg) {
    document.getElementById('messageInput').value = msg;
    sendMessage();
}

// ============================================================
// Burbujas de chat
// ============================================================

function addUserBubble(message) {
    const chatArea = document.getElementById('chatArea');
    const time = getCurrentTime();

    const wrapper = document.createElement('div');
    wrapper.className = 'chat-bubble-wrapper user';
    wrapper.innerHTML = `
        <div class="bubble-avatar user-avatar">👤</div>
        <div>
            <div class="chat-bubble user-bubble">${escapeHtml(message)}</div>
            <div class="bubble-time">${time}</div>
        </div>
    `;

    chatArea.appendChild(wrapper);
    scrollToBottom();
}

function addBotBubble(message) {
    const chatArea = document.getElementById('chatArea');
    const time = getCurrentTime();

    // Convertir markdown básico a HTML
    const formattedMessage = formatBotMessage(message);

    const wrapper = document.createElement('div');
    wrapper.className = 'chat-bubble-wrapper bot';
    wrapper.innerHTML = `
        <div class="bubble-avatar bot-avatar">🐉</div>
        <div>
            <div class="chat-bubble bot-bubble">${formattedMessage}</div>
            <div class="bubble-time">${time}</div>
        </div>
    `;

    chatArea.appendChild(wrapper);
    scrollToBottom();
}

// ============================================================
// Indicador de escritura
// ============================================================

function showTypingIndicator() {
    const chatArea = document.getElementById('chatArea');

    const wrapper = document.createElement('div');
    wrapper.className = 'chat-bubble-wrapper bot';
    wrapper.id = 'typingIndicator';
    wrapper.innerHTML = `
        <div class="bubble-avatar bot-avatar">🐉</div>
        <div class="chat-bubble bot-bubble">
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        </div>
    `;

    chatArea.appendChild(wrapper);
    scrollToBottom();
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) indicator.remove();
}

// ============================================================
// Barra de intención
// ============================================================

function updateIntentBar(intent, confidence) {
    const intentValue = document.getElementById('intentValue');
    const confidenceValue = document.getElementById('confidenceValue');
    const confidenceBar = document.getElementById('confidenceBar');

    const displayIntent = intent === 'desconocida' ? '🤔 No reconocida' : intent.replace(/_/g, ' ');
    intentValue.textContent = displayIntent;
    confidenceValue.textContent = (confidence * 100).toFixed(1) + '%';
    confidenceBar.style.width = (confidence * 100) + '%';

    // Color según confianza
    if (confidence >= 0.7) {
        confidenceValue.style.color = '#22c55e';
    } else if (confidence >= 0.4) {
        confidenceValue.style.color = 'var(--dorado)';
    } else {
        confidenceValue.style.color = 'var(--rojo-claro)';
    }
}

// ============================================================
// Animación de capas de red neuronal
// ============================================================

function animateNNLayers() {
    const layers = document.querySelectorAll('.nn-layer');
    layers.forEach((layer, i) => {
        setTimeout(() => {
            layer.classList.add('active');
            setTimeout(() => layer.classList.remove('active'), 600);
        }, i * 200);
    });
}

// ============================================================
// Partículas de fondo (luciérnagas / energía)
// ============================================================

function initParticles() {
    const container = document.getElementById('bgParticles');
    const colors = ['var(--jade)', 'var(--dorado)', 'var(--rojo-imperial)'];

    for (let i = 0; i < 25; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.width = (Math.random() * 4 + 2) + 'px';
        particle.style.height = particle.style.width;
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];
        particle.style.animationDuration = (Math.random() * 10 + 8) + 's';
        particle.style.animationDelay = (Math.random() * 10) + 's';
        particle.style.boxShadow = `0 0 6px ${colors[Math.floor(Math.random() * colors.length)]}`;
        container.appendChild(particle);
    }
}

// ============================================================
// Rotación de frases del footer
// ============================================================

function rotateFooterQuotes() {
    const quoteEl = document.getElementById('footerQuote');
    let currentIndex = 0;

    setInterval(() => {
        currentIndex = (currentIndex + 1) % QUOTES.length;
        quoteEl.style.opacity = '0';
        setTimeout(() => {
            quoteEl.textContent = QUOTES[currentIndex];
            quoteEl.style.opacity = '0.6';
        }, 500);
    }, 8000);
}

// ============================================================
// Eventos de teclado
// ============================================================

function initKeyboardEvents() {
    const input = document.getElementById('messageInput');
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
}

// ============================================================
// Utilidades
// ============================================================

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatBotMessage(message) {
    // Convertir **texto** a <strong>texto</strong>
    let formatted = message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Convertir *texto* a <em>texto</em>
    formatted = formatted.replace(/\*(.*?)\*/g, '<em>$1</em>');
    // Convertir \n a <br>
    formatted = formatted.replace(/\n/g, '<br>');
    // Convertir • a bullets estilizados
    formatted = formatted.replace(/•/g, '<span style="color: var(--jade-claro);">•</span>');
    return formatted;
}

function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('es-MX', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

function scrollToBottom() {
    const chatArea = document.getElementById('chatArea');
    setTimeout(() => {
        chatArea.scrollTop = chatArea.scrollHeight;
    }, 50);
}

function hideWelcome() {
    const welcome = document.querySelector('.welcome-message');
    if (welcome) {
        welcome.style.transition = 'all 0.3s ease-out';
        welcome.style.opacity = '0';
        welcome.style.transform = 'translateY(-10px)';
        setTimeout(() => welcome.remove(), 300);
    }
}
