const TelegramBot = require("node-telegram-bot-api");
// import axios from "axios";

const token = process.env.TELEGRAM_BOT_TOKEN || "";
// const botServiceURL = process.env.BOT_SERVICE_URL || "";

const bot = new TelegramBot(token, { polling: true });

bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  console.log(msg);
  // const text = msg.text;

  try {
    // const response = await axios.post(botServiceURL, {
    //   user_id: chatId,
    //   message: text,
    // });

    bot.sendMessage(chatId, `${msg.text} expense added`);
  } catch (error) {
    console.error(error);
    bot.sendMessage(chatId, "An error occurred while processing your message.");
  }
});
