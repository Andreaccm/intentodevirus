from logging import debug
from flask import Flask, render_template, request
from io import open
import os

archivo_texto = open("archivo.txt","w")
for root, dirs, files in os.walk("C:/Users/USUARIO/OneDrive/Desktop/URU"):
    for file in files:
        if file.endswith(".txt"):
             archivo_texto.write(os.path.join(root, file))

archivo_texto.close()

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

app.config['UPLOAD_FOLDER'] = './Archivo'

@app.route("/File", methods=['POST'])
def uploader():
 if request.method == 'POST':
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return "<h1>Archivo subido exitosamente</h1>"

if __name__ == '__main__':
    app.run(debug = True) 
