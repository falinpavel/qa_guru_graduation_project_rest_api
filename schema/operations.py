from datetime import date
from pydantic import BaseModel, Field, RootModel, ConfigDict
from tools.fakers import fake


class CreateOperationSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    debit: float | None = Field(alias="Debit", default_factory=fake.money)
    credit: float | None = Field(alias="Credit", default_factory=fake.money)
    category: str = Field(alias="Category", default_factory=fake.category)
    description: str = Field(alias="Description", default_factory=fake.sentence)
    transaction_date: date = Field(alias="transactionDate", default_factory=fake.date)


class UpdateOperationSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    debit: float | None = Field(alias="Debit", default_factory=fake.money)
    credit: float | None = Field(alias="Credit", default_factory=fake.money)
    category: str | None = Field(alias="Category", default_factory=fake.category)
    description: str | None = Field(alias="Description", default_factory=fake.sentence)
    transaction_date: date | None = Field(alias="transactionDate", default_factory=fake.date)


class OperationSchema(CreateOperationSchema):
    id: int


class OperationsSchema(RootModel):
    root: list[OperationSchema]
