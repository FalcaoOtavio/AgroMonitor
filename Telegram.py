import telebot
from API_Key import API_Telegram
import requests
import schedule
import time

API = API_Telegram

url = "https://api-agromonitor-production.up.railway.app/getData"

bot = telebot.TeleBot(API)

print('Bot Telegram INICIADO')

def get_and_send_data(chat_id):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['temperature']
        humidity = data['humidity']
        message = f"Temperature: {temperature}°C\nHumidity: {humidity}%"
        bot.send_message(chat_id, message)

@bot.message_handler(commands=['start'])
def start(mensagem):
    text = 'Welcome back, BOT Notification AgroMonitor is start!'
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['now'])
def send_now_data(mensagem):
    get_and_send_data(mensagem.chat.id)

@bot.message_handler(commands=['send'])
def send_data_periodically(mensagem):
    chat_id = mensagem.chat.id
    get_and_send_data(chat_id)
    schedule.every(3).hours.do(get_and_send_data, chat_id)
    
bot.polling(non_stop=True)
while True:
    schedule.run_pending()
    time.sleep(1)

