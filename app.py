from flask import Flask, render_template, request, jsonify
from database import load_jobs_from_db, load_job_from_db, add_application_to_db



app = Flask(__name__)

UPLOADS = [
  {
    'id' : 1,
    'title' : 'Resume',
    'price' : 'Free',
    'uploads' : 'Unlimited'
    
  },
  {
    'id' : 2,
    'title' : 'Certificates',
    'price' : 'Free',
    'uploads' : 'Unlimited'
  },
  {
    'id' : 3,
    'title' : 'Recognitions',
    'price' : 'Free',
    'uploads' : 'Unlimited'
  }

]


@app.route("/")
def bismillah():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         uploads=jobs)

@app.route("/api/uploads")
def list_uploads():
  jobs = load_jobs_from_db()
  return jsonify(UPLOADS)

@app.route("/upload/<int:id>")
def show_upload(id):
  upload = load_job_from_db(id)
  if not upload:
    return "Not Found", 404
  else:
    return render_template('uploadpage.html', upload=upload)



@app.route("/upload/<int:id>/apply", methods=['post'])
def apply_to_uplaod(id):
  data = request.form
  upload = load_job_from_db(id)

  add_application_to_db(id, data)
  #store in db
  #send an email
  #display an ack
  # return data
  return render_template('application_submitted.html', application=data, upload=upload)
  

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug =True)