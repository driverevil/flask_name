from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    minuscula = False
    mayuscula = False
    numero = False
    first = request.args.get('first')

    minuscula = any(c.islower() for c in first)  # alguna min
    mayuscula = any(c.isupper() for c in first)  # alguna mayusc
    numero = first[-1].isdigit()  # numero al final

    report = minuscula and mayuscula and numero

    return render_template('report.html', report=report, min=minuscula, may=mayuscula, num=numero)


if __name__ == '__main__':
    app.run(debug=True)
