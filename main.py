from flask import Flask, render_template

app = Flask(__name__)

DATES = [
  {
    'id': 1,
    'date': '7 May 2023'
  },
  {
    'id': 2,
    'date': '13 May 2023'
  },
  {
    'id': 3,
    'date': '16 May 2023'
  },
  {
    'id': 4,
    'date': '17 May 2023'
  },
]

@app.route("/")
def home():
  return render_template('home.html', dates = DATES)

if __name__ == "__main__":
  app.run(host='0.0.0.0')