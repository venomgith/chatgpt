import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '' #your_tg_key

openai.api_key = '' #your_api_key_chatgpt

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You: "]
        )
        await message.answer(response['choices'][0]['text'])
    except Exception as e:
        await message.answer(f"Error: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)