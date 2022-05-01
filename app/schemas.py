from marshmallow import Schema, fields, post_load
from .models import Protein

'''
funzione che trasformi pubmedid in url
 validation per tutti che assicuri, nessun campo sia vuoto, validate nullable = False
 post_load per creare un'istanza Protein con i valori inseriti campi
required=True   validates
fields.Function(lambda obj: ...)   strip pubmedid url
'''

class ProteinSchema(Schema):
    id = fields.Int(dump_only=True)
    ENTRY_NAME = fields.Str()
    PROTEIN_NAME = fields.Str()
    CHROMOSOME_NAME = fields.Str()
    GENE_NAME = fields.Str()
    STRAND = fields.Number()
    PEPTIDE_SEQUENCE = fields.Str()
    PEPTIDE_MASS = fields.Number()
    PUBMEDID = fields.Str(allow_none=True)

    @post_load
    def make_protein(self, data, **kwargs):
        return Protein(**data)  #data can contain 1 or more objects

