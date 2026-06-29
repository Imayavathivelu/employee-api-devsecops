from database import db
from models.employee import Employee

def get_all_employees():
    return Employee.query.all()

def get_employee(employee_id):
    return Employee.query.get(employee_id)

def create_employee(data):
    employee = Employee(
        name=data["name"],
        department=data["department"],
        salary=data["salary"]
    )

    db.session.add(employee)
    db.session.commit()

    return employee

def update_employee(employee, data):
    employee.name = data["name"]
    employee.department = data["department"]
    employee.salary = data["salary"]

    db.session.commit()

    return employee

def delete_employee(employee):
    db.session.delete(employee)
    db.session.commit()