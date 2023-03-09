from flask import Flask, render_template, jsonify

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
  return render_template('home.html', uploads = UPLOADS)

@app.route("/api/uploads")
def list_uploads():
  return jsonify(UPLOADS)
  

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug =True)