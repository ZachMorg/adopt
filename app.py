from flask import Flask, render_template, flash, redirect
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'Password123_lol'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


connect_db(app)
with app.app_context():
    db.create_all()


@app.route('/')
def home_page():

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/pets/new', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/pets/<int:pet_id>', methods=['GET', 'POST'])
def pet_deets(pet_id):

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_deets.html', form=form, pet=pet)