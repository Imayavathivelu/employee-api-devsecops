from flask import Blueprint, request, jsonify

from services.employee_services import (
    get_all_employees,
    get_employee,
    create_employee,
    update_employee,
    delete_employee
)

employee_bp = Blueprint("employees", __name__)

@employee_bp.route("/employees", methods=["GET"])
def employees():
    employees = get_all_employees()
    return jsonify([employee.to_dict() for employee in employees])

@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def employee(employee_id):
    employee = get_employee(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee.to_dict())

@employee_bp.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    employee = create_employee(data)
    return jsonify(employee.to_dict()), 201

@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def edit_employee(employee_id):
    employee = get_employee(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    data = request.get_json()
    employee = update_employee(employee, data)
    return jsonify(employee.to_dict())

@employee_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def remove_employee(employee_id):
    employee = get_employee(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    delete_employee(employee)
    return jsonify({"message": "Employee deleted successfully"})