from flask import Flask,render_template,request
from formularios import DatosImc
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())

@app.route("/",methods=["GET","POST"])
def welcome():
    form = DatosImc()
    if form.validate_on_submit():
        peso = form.peso.data
        talla = form.talla.data
        return render_template("index.html",form=form)
    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)
