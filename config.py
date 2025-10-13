from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    """
    Настройки HTTP-клиента.

    Поля:
        url (HttpUrl): Базовый URL для API.
        timeout (float): Таймаут для запросов в секундах.
    """
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        """
        Возвращает URL API в строковом формате.
        """
        return str(self.url)


class Settings(BaseSettings):
    """
    Главная модель для хранения всех настроек проекта.

    Загружает переменные из файла `.env` и поддерживает вложенные структуры.

    Поля:
        fake_bank_http_client (HTTPClientConfig): Настройки HTTP-клиента.
    """
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )
    fake_bank_http_client: HTTPClientConfig
