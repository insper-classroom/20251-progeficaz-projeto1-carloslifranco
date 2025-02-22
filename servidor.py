from flask import Flask, render_template_string, request, redirect
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete_note/<int:id>', methods=['GET'])
def delete_note(id):
    views.delete_note(id)
    return redirect('/')

# @app.route('/edit_note/<int:id>', methods=['POST', 'GET'])
# def edit_note(id):
#     views.edit_note(id)
#     return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)