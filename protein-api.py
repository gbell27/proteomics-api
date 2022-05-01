import os
from app import create_app, db
from app.models import Protein
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Protein=Protein)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def populate():
    """Populate database"""
    from population_script import proteins
    db.drop_all()
    db.create_all()
    db.session.add_all(proteins)
    db.session.commit()
