from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or request.form
    try:
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        if height <= 0:
            raise ValueError('Altura debe ser mayor que 0')
        imc = weight / (height ** 2)
        imc_rounded = round(imc, 2)
        if imc < 18.5:
            classification = 'Bajo peso'
        elif imc < 25:
            classification = 'Peso saludable'
        elif imc < 30:
            classification = 'Sobrepeso'
        else:
            classification = 'Obesidad'
        return jsonify({'imc': imc_rounded, 'classification': classification})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
