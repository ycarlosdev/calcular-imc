from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from formularios import DatosImc, LoginUser,  RegisterUser
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from imc import calcular_imc
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuraciones generales
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Permite la gestion de logeo del usuario
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Permitiendo la gestion del uso de base de datos
db = SQLAlchemy(app)


# Modelo para guardar los datos del usuario en la db

class User(UserMixin,db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120) , nullable = False)
    password = db.Column(db.String(120) , nullable = False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    @staticmethod
    def get_by_id(id):
        return User.query.get(id) 

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()


# Endpoints de la aplicacion web
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


@app.route('/login/',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginUser()

    if form.validate_on_submit():
        email = form.email.data
        user  = User.get_by_email(email)

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
        name = form.name.data
        email = form.email.data
        password =  form.password.data
        user = User(name=name, email=email, password=password)

        # Guardar usuario en la base de datos
        db.session.add(user)
        db.session.commit()

        login_user(user,remember=True) # Logueando al usuario
        next_page = request.args.get('next',None)

        if not next_page:
            next_page = url_for('home')

        return redirect(next_page)
    
    return render_template('register.html',form = form)


# Permitir trabajar con el usuario en sesion
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

# Permitir Logout al usuario
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Creamos las tablas dentro del Application Context
    with app.app_context():
        db.create_all()
        print("¡Base de datos SQLite ('miniblog.db') y tablas verificadas/creadas con éxito!")

    app.run(debug=True)
