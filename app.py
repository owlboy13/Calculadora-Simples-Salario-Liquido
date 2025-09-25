from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])
    except ValueError:
        return "Erro: Insira valores válidos."

    valor_dependente = 200.00
    percentual_inss = 8
    resultado = salario - (salario * percentual_inss / 100)
    resultado_dependencia = resultado + (valor_dependente * dependentes)
    resultado_formatado = f"R$ {resultado_dependencia:.2f}".replace(".", ",")
    return render_template('resultado.html', resultado=resultado_formatado)

if __name__ == '__main__':
    app.run(debug=True)
