from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)

# UPLOADS = [
#   {
#     'id' : 1,
#     'title' : 'Resume',
#     'price' : 'Free',
#     'uploads' : 'Unlimited'
    
#   },
#   {
#     'id' : 2,
#     'title' : 'Certificates',
#     'price' : 'Free',
#     'uploads' : 'Unlimited'
#   },
#   {
#     'id' : 3,
#     'title' : 'Recognitions',
#     'price' : 'Free',
#     'uploads' : 'Unlimited'
#   }

# ]


@app.route("/")
def bismillah():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         uploads=jobs)

@app.route("/api/uploads")
def list_uploads():
  jobs = load_jobs_from_db()
  return jsonify(UPLOADS)
  

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug =True)