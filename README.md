# FLASK PROTEOMICS API
This is an API based on [Proteomics API](https://www.proteomicsdb.org/#api).
Json data was fetched using:
>`https://www.proteomicsdb.org/proteomicsdb/logic/api/proteinpeptideresult.xsodata/InputParams(PROTEINFILTER='Q92769')/Results?$select=ENTRY_NAME,PROTEIN_NAME,CHROMOSOME_NAME,GENE_NAME,STRAND,PEPTIDE_SEQUENCE,PEPTIDE_MASS,PUBMEDID&$format=json`  
I left out some fields because I wanted to make a simple schema.

### ENVIRONMENT VARIABLES
Be sure to setup **FLASK\_APP** environment variable.

_**ex.**_
> `export FLASK_APP=protein-api.py`

### RUNNING APP
After setting the environment variables, you can:
1. Test the app
> `flask test`

2. Initialize DB
> `flask db init`
> `flask migrate -m "Initial migration"` will make a migration script.
> `flask db upgrade` is equivalent to calling `db.create_all()`

3. Populate DB with test data.
> `flask populate`   will add protein sequences from _cleaned-protein.json_ file.

4. Run the api locally 
(default will be localhost:5000) with
> `flask run`

## Authentication
The application uses flask-httpauth for **_JWT_** token authentication.

### TESTING HTTP REQUESTS
Using httpie
`http --json GET http://127.0.0.1:5000/api/v1/proteins/`
Either way using Postman you can receive/send json data.

#### HOW TO USE THE API
5 routes:
1. GET    http://localhost:5000/api/v1/proteins/  
  GET ALL ENTRIES
2. GET    http://localhost:5000/api/v1/protein/{id}  
  GET single entry with specified id.  **e.g. [...]/protein/5**
3. POST   http://localhost:5000/api/v1/proteins/    {json}  
  CREATE a new protein entry
4. PUT    http://localhost:5000/api/v1/protein/{id}  
  UPDATE protein's pubmed id
5. DELETE http://localhost:5000/api/v1/protein/{id}  
  DELETE protein entry with id **e.g. [...]/protein/5**
