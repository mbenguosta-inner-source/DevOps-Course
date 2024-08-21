from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_employee,
    delete_employee,
    retrieve_employee,
    retrieve_employees,
    update_employee,
)
from app.server.models.employee import (
    ErrorResponseModel,
    ResponseModel,
    EmployeeSchema,
    UpdateEmployeeModel,
)

router = APIRouter()


@router.post("/", response_description="employee data added into the database")
async def add_employee_data(employee: EmployeeSchema = Body(...)):
    employee = jsonable_encoder(employee)
    new_employee = await add_employee(employee)
    return ResponseModel(new_employee, "employee added successfully.")

@router.get("/", response_description="Employee retrieved")
async def get_employees():
    employees = await retrieve_employees()
    if employees:
        return ResponseModel(employees, "employees data retrieved successfully")
    return ResponseModel(employees, "Empty list returned")


@router.get("/{id}", response_description="employee data retrieved")
async def get_employee_data(id):
    employee = await retrieve_employee(id)
    if employee:
        return ResponseModel(employee, "employee data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "employee doesn't exist.")

@router.put("/{id}")
async def update_employee_data(id: str, req: UpdateEmployeeModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_employee = await update_employee(id, req)
    if updated_employee:
        return ResponseModel(
            "employee with ID: {} name update is successful".format(id),
            "employee name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the employee data.",
    )

@router.delete("/{id}", response_description="employee data deleted from the database")
async def delete_employee_data(id: str):
    deleted_employee = await delete_employee(id)
    if deleted_employee:
        return ResponseModel(
            "employee with ID: {} removed".format(id), "employee deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "employee with id {0} doesn't exist".format(id)
    )