from utils import *

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados[1], details=dados[2], id=dados[0])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    create_post(titulo, detalhes)

def deletar_notas(id):
    delete_note(id)

# def editar_notas(id):
#     edit_note(id)

