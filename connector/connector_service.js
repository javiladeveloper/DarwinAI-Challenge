const TelegramBot = require("node-telegram-bot-api");
const axios = require("axios");

const token = process.env.TELEGRAM_BOT_TOKEN || "";
const botServiceURL = process.env.BOT_SERVICE_URL || "";

const bot = new TelegramBot(token, { polling: true });

bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  console.log(chatId, text);
  try {
    const response = await axios.post(botServiceURL, {
      telegram_id: chatId,
      message: text,
    });
    bot.sendMessage(chatId, response.data.message);
  } catch (error) {
    console.error(error);
    bot.sendMessage(chatId, "An error occurred while processing your message.");
  }
});
