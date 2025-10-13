import pytest

from http import HTTPStatus
from clients.operations_client import OperationsClient
from schema.operations import (
    OperationsSchema,
    OperationSchema,
    CreateOperationSchema,
    UpdateOperationSchema
)
from tools.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)
from tools.assertions.base import assert_status_code
from tools.assertions.operations import assert_operation, assert_create_operation
from tools.assertions.schema import validate_json_schema


@pytest.mark.operations
@pytest.mark.regression
@allure_high_level_marks(
    epic="Operations",
    feature="Operations"
)
class TestOperations:

    @allure_mid_level_marks(
        story="User can get list of operations",
        testcase_id="CASE-1",
        title="Get list of operations",
        label="REST API",
        owner="AQA FALIN PAVEL"
    )
    @pytest.mark.xfail(
        reason="BUG-1 Response schema is not valid, credit field got string instead of float"
    )
    def test_get_operations(self, operations_client: OperationsClient):
        response = operations_client.get_operations_api()
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(),
                             schema=OperationsSchema.model_json_schema())

    @allure_mid_level_marks(
        story="User can get operation by id",
        testcase_id="CASE-2",
        title="Get operation by id",
        label="REST API",
        owner="AQA FALIN PAVEL"
    )
    def test_get_operation(self, operations_client: OperationsClient,
                           function_operation: OperationSchema):
        response = operations_client.get_operation_api(operation_id=function_operation.id)
        operation = OperationSchema.model_validate_json(json_data=response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_operation(actual=operation, expected=function_operation)
        validate_json_schema(instance=response.json(), schema=operation.model_json_schema())

    @allure_mid_level_marks(
        story="User can create new operation",
        testcase_id="CASE-3",
        title="Create operation",
        label="REST API",
        owner="AQA FALIN PAVEL"
    )
    def test_create_operation(self, operations_client: OperationsClient):
        request = CreateOperationSchema()
        response = operations_client.create_operation_api(operation=request)
        operation = OperationSchema.model_validate_json(json_data=response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        assert_create_operation(actual=operation, expected=request)
        validate_json_schema(instance=response.json(), schema=operation.model_json_schema())

    @allure_mid_level_marks(
        story="User can update operation by id",
        testcase_id="CASE-4",
        title="Update operation",
        label="REST API",
        owner="AQA FALIN PAVEL"
    )
    def test_update_operation(self, operations_client: OperationsClient,
                              function_operation: OperationSchema):
        request = UpdateOperationSchema()
        response = operations_client.update_operation_api(operation_id=function_operation.id,
                                                          operation=request)
        operation = OperationSchema.model_validate_json(json_data=response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_operation(actual=operation, expected=request)
        validate_json_schema(instance=response.json(), schema=operation.model_json_schema())

    @allure_mid_level_marks(
        story="User can delete operation by id",
        testcase_id="CASE-5",
        title="Delete operation",
        label="REST API",
        owner="AQA FALIN PAVEL"
    )
    def test_delete_operation(self, operations_client: OperationsClient,
                              function_operation: OperationSchema):
        delete_response = operations_client.delete_operation_api(operation_id=function_operation.id)
        assert_status_code(actual=delete_response.status_code, expected=HTTPStatus.OK)
        get_response = operations_client.get_operation_api(operation_id=function_operation.id)
        assert_status_code(actual=get_response.status_code, expected=HTTPStatus.NOT_FOUND)
