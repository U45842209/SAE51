from sql_interact import main
from flask import Flask, request, render_template

init = main.DATA_HOARDER()
init.connect_to_db()
app = Flask(__name__, template_folder='html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', visibility='hidden', result='Vide')
    elif request.method == 'POST':
        number = request.form.get("number")
        func = getattr(init, f'exo_{number}', None)  # Added None as a default value
        if func is not None:
            result = func()
            return render_template('index.html', visibility='visible', result=result)
        else:
            return render_template('index.html', visibility='hidden', result='Invalid number or method not found')


if __name__ == '__main__':
    app.run()
