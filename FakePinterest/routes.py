#Criar rotas do site (links)
from flask import render_template, url_for
from FakePinterest import app

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/<usuario>")
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)


