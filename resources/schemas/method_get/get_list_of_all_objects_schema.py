from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Union


class ObjectData(BaseModel):
    """Модель для данных объекта с опциональными полями"""
    color: Optional[str] = None
    capacity: Optional[str] = None
    price: Optional[Union[float, str]] = None
    generation: Optional[str] = None
    year: Optional[int] = None
    cpu_model: Optional[str] = Field(None, alias="CPU model")
    hard_disk_size: Optional[str] = Field(None, alias="Hard disk size")
    strap_colour: Optional[str] = Field(None, alias="Strap Colour")
    case_size: Optional[str] = Field(None, alias="Case Size")
    description: Optional[str] = Field(None, alias="Description")
    screen_size: Optional[Union[float, int]] = Field(None, alias="Screen size")
    capacity_gb: Optional[Union[str, int]] = Field(None, alias="Capacity GB")

    model_config = ConfigDict(extra='allow', populate_by_name=True)


class ObjectResponse(BaseModel):
    """Модель для ответа с информацией об объекте"""
    id: str
    name: str
    data: Optional[ObjectData] = None

    model_config = ConfigDict(extra='forbid')


# Просто тип для списка объектов
ObjectsList = List[ObjectResponse]
