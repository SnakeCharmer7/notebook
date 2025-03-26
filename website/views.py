from flask import Blueprint, render_template, url_for, request, flash
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
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.author == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return "", 200
    flash("Note not founded", category='error')
