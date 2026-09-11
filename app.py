from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from formularios import DatosImc, LoginUser,  RegisterUser
import uuid
from imc import calcular_imc
from  modelos import users,get_user,User

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())

# Permite la gestion de logeo del usuario
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route("/",methods=["GET","POST"])
@login_required
def home():
    form = DatosImc()
    if form.validate_on_submit():
        peso = form.peso.data
        unidad_medida_peso = request.form.get('unidad-peso')
        print(unidad_medida_peso)
        
        talla = form.talla.data
        unidad_medida_talla = request.form.get('unidad-talla')
        imc = calcular_imc(peso,unidad_medida_peso,talla,unidad_medida_talla)
        return render_template("index.html",form=form,imc = imc)
    return render_template("index.html",form=form)

@app.route("/apoyanos/")
def apoyanos():
    return render_template("apoyanos.html")

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/login/',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginUser()

    if form.validate_on_submit():
        email = form.email.data
        user  = get_user(email)

        if user is not None:
            login_user(user,remember=form.remember_me.data)
            next_page = request.args.get('next')

            if not next_page:
                next_page = url_for('home')
            
            return redirect(next_page)
    
    return render_template('login.html',form = form)

@app.route('/register/',methods=['GET','POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterUser()

    if form.validate_on_submit():
        id = len(users) + 1
        name = form.name.data
        email = form.email.data
        password =  form.password.data
        user = User(id,name,email,password)
        users.append(user)

        login_user(user,remember=True)
        next_page = request.args.get('next',None)

        if not next_page:
            next_page = url_for('home')

        return redirect(next_page)
    
    return render_template('register.html',form = form)

# Permitir Logout al usuario
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
