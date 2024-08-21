from typing import Optional

from pydantic import BaseModel, Field




class EmployeeSchema(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    profile: str = Field(...)
    salary: float = Field(..., gt=0)
    integration: int = Field(..., gt=0)

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName":"Doe",
                "profile":"Data Engineer",
                "salary": "40000",
                "integration": 2020
            }
        }


class UpdateEmployeeModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    rofile: Optional[str]
    salary: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName":"Doe",
                "profile":"Data Engineer",
                "salary": "40000",
                "integration": 2020
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
