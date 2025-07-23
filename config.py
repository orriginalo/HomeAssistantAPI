from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv(override=True)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

SERVER_IP = "http://192.168.1.61"
QBITTORRENT_USERNAME = "admin"
QBITTORRENT_PASSWORD = "42La596mumia54"

class SystemPrompts(Enum):
    EXTRACT_KINO_NAME= """
  Ты парсер. Получаешь объект с двумя полями:

type: movie | show | collection
text: пользовательский запрос

Твоя задача — извлечь только название фильма, сериала или коллекции согласно type. Не добавляй ничего, не перефразируй. Если название не указано — верни пустую строку.

Примеры:

Вход:
type: movie
text: скачай интерстеллар
Выход:
Интерстеллар

Вход:
type: show
text: хочу посмотреть во все тяжкие
Выход:
Во все тяжкие

Вход:
type: collection
text: найди мне марвел фильмы
Выход:
Марвел
    """
    
    EXTRACT_CONTAINERNAME = """
    
    """
    