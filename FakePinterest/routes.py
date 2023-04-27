#Criar rotas do site (links)
from flask import render_template, url_for, redirect
from FakePinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.forms import FormLogin, FormRegistro
from FakePinterest.models import Usuario, Foto


@app.route("/", methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", usuario=usuario.username))

    return render_template('home.html', form=formlogin)



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    formregistro = FormRegistro()
    if formregistro.validate_on_submit():
        senha = bcrypt.generate_password_hash(formregistro.senha.data)


        usuario = Usuario(username=formregistro.username.data, email=formregistro.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", usuario=usuario.username))
    return render_template('registro.html', form=formregistro)



@app.route("/<usuario>")
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))