from flask import Blueprint, request, jsonify
from app.services.mongo_service import MongoService
from app.models.benefit import Benefit
from bson import ObjectId
from cerberus import Validator

benefit_bp = Blueprint('benefit', __name__)
mongo_service = MongoService()

def convert_objectid_to_str(data):
    if isinstance(data, list):
        for item in data:
            if '_id' in item:
                item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        if '_id' in data:
            data['_id'] = str(data['_id'])
    return data

# Define a validation schema for a benefit
benefit_schema = {
    'name': {'type': 'string', 'required': True, 'empty': False},
    'description': {'type': 'string', 'required': True, 'empty': False},
    'provider': {'type': 'string', 'required': True, 'empty': False},
    'expiration_date': {'type': 'string', 'required': True, 'empty': False},
}

validator = Validator(benefit_schema)

@benefit_bp.route('/benefits', methods=['POST'])
def create_benefit():
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": validator.errors}), 400
    new_benefit = Benefit(data)
    benefit_id = mongo_service.create_benefit(Benefit.to_json(new_benefit))
    return jsonify({"message": "Benefit created", "id": str(benefit_id)}), 201

@benefit_bp.route('/benefits/<benefit_id>', methods=['GET'])
def get_benefit(benefit_id):
    benefit = mongo_service.get_benefit(ObjectId(benefit_id))
    if benefit:
        benefit = convert_objectid_to_str(benefit)
        return jsonify(benefit), 200
    return jsonify({"error": "Benefit not found"}), 404

@benefit_bp.route('/benefits/<benefit_id>', methods=['PUT'])
def update_benefit(benefit_id):
    data = request.json
    updated = mongo_service.update_benefit(ObjectId(benefit_id), data)
    if updated.modified_count > 0:
        return jsonify({"message": "Benefit updated"}), 200
    return jsonify({"error": "Benefit not found or no changes made"}), 404

@benefit_bp.route('/benefits/<benefit_id>', methods=['DELETE'])
def delete_benefit(benefit_id):
    deleted = mongo_service.delete_benefit(ObjectId(benefit_id))
    if deleted.deleted_count > 0:
        return jsonify({"message": "Benefit deleted"}), 200
    return jsonify({"error": "Benefit not found"}), 404

@benefit_bp.route('/benefits', methods=['GET'])
def get_all_benefits():
    benefits = mongo_service.get_all_benefits()
    benefits = convert_objectid_to_str(benefits)
    return jsonify(benefits), 200
