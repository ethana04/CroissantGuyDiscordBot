from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
<<<<<<< HEAD
  return "The croissant is in the boulangerie !"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
=======
    return "Croissant is online !"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t=Thread(target=run)
    t.start()
>>>>>>> d1dffe763f336615c37f5a03a5667d298e7c2bf6
