import requests
from pyrogram import Client, filters

def init(app):

    @app.on_message(filters.command('ask', prefixes = '.') & filters.me)
    def ask_ai(client, message):

        # Получаем текст запроса от пользователя
        user_query = message.text.split(' ', maxsplit = 1)[1]

        # Устанавливаем сообщение 'Загрузка...'
        message.edit_text('<b><emoji id="5440621591387980068">🔄</emoji> Загрузка...</b>')

        try:
            # Отправляем запрос к API
            url = f'https://inquisitive-grizzly-conkerberry.glitch.me/?ask={user_query}&model=gemini'
            response = requests.get(url)

            # Проверяем, успешен ли запрос (Статус 200)
            if response.status_code == 200:
                ai_response = response.text or '<b><emoji id = "5199885118214255386">🤖</emoji> Нет ответа от ИИ.</b>'
            else:
                ai_response = f'<b><emoji id="5447644880824181073">⚠️</emoji> Ошибка: Код ответа {response.status_code}</b>'

        except Exception as e:
            ai_response = f'<b><emoji id="5240241223632954241">❌</emoji> Произошла ошибка: {e}</b>'

        # Обновляем сообщение, заменяя его на ответ от ИИ
        message.edit_text(f'<b><emoji id="5443038326535759644">💬</emoji> Вопрос: {user_query}\n\nОтвет: {ai_response}</b>')