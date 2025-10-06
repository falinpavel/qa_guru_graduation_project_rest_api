import pytest

from clients.operations_client import OperationsClient
from schema.operations import OperationSchema


@pytest.fixture
def operations_client(settings) -> OperationsClient:
    from clients.operations_client import get_operations_client
    return get_operations_client(settings)


@pytest.fixture
def function_operation(operations_client: OperationsClient) -> OperationSchema:
    operation = operations_client.create_operation()
    yield operation
    operations_client.delete_operation_api(operation.id)
