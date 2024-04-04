// Importa el módulo node-telegram-bot-api para interactuar con la API de Telegram
const TelegramBot = require("node-telegram-bot-api");
// Importa el módulo axios para realizar solicitudes HTTP
const axios = require("axios");

// Obtiene el token del bot de Telegram y la URL del servicio backend de las variables de entorno
const token = process.env.TELEGRAM_BOT_TOKEN || "";
const botServiceURL = process.env.BOT_SERVICE_URL || "";

// Crea una instancia del bot de Telegram con el token y habilita el modo polling
const bot = new TelegramBot(token, { polling: true });

// Escucha el evento 'message' que se activa cuando el bot recibe un mensaje
bot.on("message", async (msg) => {
  // Obtiene el ID del chat y el texto del mensaje recibido
  const chatId = msg.chat.id;
  const text = msg.text;

  // Muestra en la consola el ID del chat y el texto del mensaje
  console.log(chatId, text);

  try {
    // Envía una solicitud POST al servicio backend con el ID del chat y el mensaje como datos
    const response = await axios.post(botServiceURL, {
      telegram_id: chatId,
      message: text,
    });

    // Envía al chat la respuesta recibida del servicio backend
    bot.sendMessage(chatId, response.data.message);
  } catch (error) {
    // En caso de error, muestra el error en la consola y envía un mensaje de error al chat
    console.error(error);
    bot.sendMessage(chatId, "An error occurred while processing your message.");
  }
});
