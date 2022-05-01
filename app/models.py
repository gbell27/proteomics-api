from . import db

class Protein(db.Model):
    __tablename__ = 'proteins'
    id = db.Column(db.Integer, primary_key=True)
    ENTRY_NAME = db.Column(db.String(64)) 
    PROTEIN_NAME = db.Column(db.String(256))
    CHROMOSOME_NAME = db.Column(db.String(2))
    GENE_NAME = db.Column(db.String(128))
    STRAND = db.Column(db.Integer)
    PEPTIDE_SEQUENCE = db.Column(db.String(500))
    PEPTIDE_MASS = db.Column(db.Float, index=True)  #double
    PUBMEDID = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Protein %r>' % self.PROTEIN_NAME
