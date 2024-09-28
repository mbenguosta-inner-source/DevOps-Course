import motor.motor_asyncio
from bson.objectid import ObjectId
import os
#MONGO_DETAILS = "mongodb://{db_user}:{db_pwd}@{db_host}:{db_port}/".format(db_user=os.environ["DATABASE_USER"], db_pwd=os.environ["DATABASE_PASSWORD"], db_host=os.environ["DATABASE_HOST"], db_port=os.environ["DATABASE_PORT"])
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI"])
database = client.employees
employee_collection = database.get_collection("employees_collection")


def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "firstName": employee["firstName"],
        "lastName": employee["lastName"],
        "profile": employee["profile"],
        "salary": employee["salary"],
        "integration": employee["integration"]
        }

# Retrieve all employees present in the database
async def retrieve_employees():
    employees = []
    async for employee in employee_collection.find():
        employees.append(employee_helper(employee))
    return employees


# Add a new employee into to the database
async def add_employee(employee_data: dict) -> dict:
    employee = await employee_collection.insert_one(employee_data)
    new_employee = await employee_collection.find_one({"_id": employee.inserted_id})
    return employee_helper(new_employee)


# Retrieve a employee with a matching ID
async def retrieve_employee(id: str) -> dict:
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


# Update a employee with a matching ID
async def update_employee(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        updated_employee = await employee_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_employee:
            return True
        return False


# Delete a employee from the database
async def delete_employee(id: str):
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        await employee_collection.delete_one({"_id": ObjectId(id)})
        return True
