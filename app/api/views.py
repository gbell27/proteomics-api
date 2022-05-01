from flask import jsonify, request, make_response
from . import api
from .. import db
from ..models import Protein
from ..schemas import ProteinSchema
from sqlalchemy.exc import IntegrityError

protein_schema = ProteinSchema()
proteins_schema = ProteinSchema(many=True)

@api.route('/proteins/', methods=["GET"])
def get_proteins():
    proteins = Protein.query.all()
    results = proteins_schema.dump(proteins)
    return make_response(jsonify({'proteins': results}))

@api.route('/protein/<int:pk>', methods=["GET"])
def get_protein_by_id(pk):
    protein = Protein.query.get(pk)
    if protein is None:
        return make_response(jsonify({'message' : 'Protein could not be found'}), 400)
    result = protein_schema.dump(protein)
    return make_response(jsonify({'protein' : result}))

@api.route('/proteins/', methods=["POST"])
def create_protein():
    json_data = request.get_json()
    if not json_data:
        return make_response(jsonify({'message': 'No input data provided'}), 400)
    protein = protein_schema.load(json_data) #add errors

    #Check if entry already exists in DB
    
    db.session.add(protein)
    db.session.commit()
    result = protein_schema.dump(Protein.query.get(protein.id))
    return make_response(jsonify({'message' : 'Created new protein entry', \
                                  'protein' : result}))


@api.route('/protein/<int:pk>', methods=["PUT"])   
def update_protein_pubmed(pk):
    protein = Protein.query.get(pk)
    if protein is None:
        return make_response(jsonify({'message': 'Protein could not be found'}), 400)
    json_data = request.get_json()
    if not json_data:
        return make_response(jsonify({'message': 'No input data provided'}), 400)
    protein.PUBMEDID = json_data['PUBMEDID']
    db.session.add(protein)
    db.session.commit()
    result = protein_schema.dump(Protein.query.get(protein.id))
    return make_response(jsonify({'message' : 'Updated protein PUBMED entry', \
                                  'protein' : result}))

@api.route('/protein/<int:pk>', methods=["DELETE"])
def delete_protein(pk):
    protein = Protein.query.get(pk)
    if protein is None:
        return make_response(jsonify({'message': 'Protein could not be found'}), 400)
    db.session.delete(protein)
    db.session.commit()
    result = protein_schema.dump(protein)
    return make_response(jsonify({'message' : 'Protein successfully removed', \
                                  'protein' : result })) # 204 NO CONTENT
