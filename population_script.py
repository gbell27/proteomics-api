import json
from app.schemas import ProteinSchema

proteins_schema = ProteinSchema(many=True)

with open('protein.json') as f:
    json_data = json.loads(f.read())

proteins = proteins_schema.load(json_data)
