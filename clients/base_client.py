import requests

from typing import Any, Optional
from urllib.parse import urljoin

from allure_commons._allure import step

from config import HTTPClientConfig
from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def log_request(method: str, url: str):
    logger.info(f"Make {method} request to {url}")


def log_response(status_code: int, reason: str, url: str):
    logger.info(f"Got response {status_code} {reason} from {url}")


class BaseClient:
    def __init__(self, base_url: str, timeout: float):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    @step("Make GET request to {url}")
    def get(self, url: str, params: Optional[dict] = None) -> requests.Response:
        full_url = urljoin(self.base_url, url)
        log_request("GET", full_url)
        response = self.session.get(full_url, params=params, timeout=self.timeout)
        log_response(response.status_code, response.reason, full_url)
        return response

    @step("Make POST request to {url}")
    def post(self, url: str, json: Any = None, data: Any = None, files: Any = None) -> requests.Response:
        full_url = urljoin(self.base_url, url)
        log_request("POST", full_url)
        response = self.session.post(full_url, json=json, data=data, files=files, timeout=self.timeout)
        log_response(response.status_code, response.reason, full_url)
        return response

    @step("Make PATCH request to {url}")
    def patch(self, url: str, json: Any = None) -> requests.Response:
        full_url = urljoin(self.base_url, url)
        log_request("PATCH", full_url)
        response = self.session.patch(full_url, json=json, timeout=self.timeout)
        log_response(response.status_code, response.reason, full_url)
        return response

    @step("Make DELETE request to {url}")
    def delete(self, url: str) -> requests.Response:
        full_url = urljoin(self.base_url, url)
        log_request("DELETE", full_url)
        response = self.session.delete(full_url, timeout=self.timeout)
        log_response(response.status_code, response.reason, full_url)
        return response


def get_http_client(config: HTTPClientConfig) -> BaseClient:
    return BaseClient(base_url=config.client_url, timeout=config.timeout)
