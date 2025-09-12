import pytest
import requests
from resources.schemas.method_get.get_list_of_all_objects_schema import ObjectResponse


class TestSimpleProductsAPI:
    BASE_URL = "https://api.restful-api.dev/objects"

    def test_get_all_objects_simple(self):
        """Упрощенный тест без сложных моделей"""
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200

        objects_data = response.json()

        # Простая валидация каждого объекта
        for obj_data in objects_data:
            # Валидируем через Pydantic
            obj = ObjectResponse(**obj_data)

            # Базовые проверки
            assert obj.id is not None
            assert obj.name is not None
            assert isinstance(obj.id, str)
            assert isinstance(obj.name, str)

            # data может быть None или объектом
            if obj.data is not None:
                # Если data есть, проверяем что это словарь с данными
                data_dict = obj.data.model_dump(exclude_none=True)
                assert len(data_dict) > 0

    def test_get_single_object_simple(self):
        """Простой тест одного объекта"""
        response = requests.get(f"{self.BASE_URL}/1")
        assert response.status_code == 200

        obj_data = response.json()
        obj = ObjectResponse(**obj_data)

        # Проверяем структуру
        assert hasattr(obj, 'id')
        assert hasattr(obj, 'name')
        assert hasattr(obj, 'data')

        print(f"Объект: {obj.id}, {obj.name}")
