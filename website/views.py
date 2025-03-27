from flask import Blueprint, render_template, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form["note"]

        if len(note) < 1:
            flash("Note is too short!", category='error')
        else:
            new_note = Note(text=note, author=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')

    return render_template("home.html", user=current_user)


@views.route("/delete_note/<int:note_id>", methods=["DELETE"])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.author == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return "", 200
    flash("Note not founded", category='error')


@views.route("/edit_note_modal/<int:note_id>", methods=["GET"])
@login_required
def edit_note_modal(note_id):
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Notatka nie znaleziona"}), 404

    return f'''
        <form hx-patch="{url_for('views.update_note', note_id=note.id)}"
              hx-target="#note-{note.id}"
              hx-swap="outerHTML"
              onsubmit="closeModal(); return true;">
              
            <textarea name="text" class="form-control" rows="10" autofocus>{note.text}</textarea>
            
            <div class="mt-3 text-end">
                <button type="submit" class="btn btn-success w-100">Save</button>
            </div>
        </form>
    '''


@views.route("/update_note/<int:note_id>", methods=["PATCH"])
@login_required
def update_note(note_id):
    note = Note.query.get(note_id)
    new_text = request.form.get("text").strip()
    if new_text:
        note.text = new_text
        db.session.commit()

    return f'''
        <li class="list-group-item d-flex align-items-center" id="note-{note.id}">
            <span class="me-auto">{new_text.replace("\n", "<br>")}</span>

            <button class="btn me-2"
                    hx-get="{url_for('views.edit_note_modal', note_id=note.id)}"
                    hx-target="#edit-modal-content"
                    hx-trigger="click"
                    data-bs-toggle="modal" data-bs-target="#editModal">
                <i class="bi bi-pencil"></i>
            </button>

            <button type="button" class="btn-close"
                    hx-delete="{url_for('views.delete_note', note_id=note.id)}"
                    hx-target="#note-{note.id}"
                    hx-swap="outerHTML">
            </button>
        </li>
    '''
