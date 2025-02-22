from flask import Flask, render_template_string, request, redirect, url_for, render_template
import views
import os
from views import *

app = Flask(__name__, template_folder=os.path.abspath('templates'))

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

# Rota para exibir o formulário de edição
@app.route('/edit_note/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    if request.method == 'POST':
        new_text = request.form['note']
        update_note(id, new_text)
        return redirect(url_for('edit_note', id=id))  # Redireciona após salvar

    # Se for GET, exibe o formulário com a anotação atual
    note = get_note(id)
    if note is None:
        return "Nota não encontrada", 404
    return render_template('edit_note.html', note=note, id=id)


if __name__ == '__main__':
    app.run(debug=True)