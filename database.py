import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args = {
    "ssl" : {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    results_as_dict = result.mappings().all()
    jobs = []
    for row in results_as_dict:
      jobs.append(row)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])

def add_application_to_db(upload_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (upload_id, full_name, email, certification_name, ca, myfile) VALUES (:upload_id, :full_name, :email, :certification_name,:ca,:myfile);")

    conn.execute(query, 
                 {"upload_id": upload_id,                       
                  "full_name":data['full_name'],"email":data['email'],                 
                  "certification_name":data['certification_name'],             
                  "ca":data['certificate_issuing_aurhority'],
                  "myfile":data['myfile']}
    )
                
    
  

  




              


                      
