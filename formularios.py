from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,StringField,EmailField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class DatosImc(FlaskForm):
    peso = FloatField('Peso',validators=[DataRequired()])
    talla = FloatField('Talla',validators=[DataRequired()])
    calcular = SubmitField('Calcular IMC',validators=[DataRequired()])

class LoginUser(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Contraseña',validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField()

class RegisterUser(FlaskForm):
    name = StringField('Nombre',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Contraseña',validators=[DataRequired()])
    submit = SubmitField()
