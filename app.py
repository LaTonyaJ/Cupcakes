from werkzeug.utils import redirect
from forms import AddCupcake
from flask import Flask, jsonify, request
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

app.config['SECRET_KEY'] = 'yummyyummydelicousness'
debug = DebugToolbarExtension(app)


def serialize(cupcake):
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }


@app.route('/api/cupcakes')
def show_cupcakes():

    cupcakes = Cupcake.query.all()
    serialized = [serialize(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:id>')
def show_single_cupcake(id):

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=serialize(cupcake))


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    new_cc = Cupcake(flavor=request.json["flavor"],
                     size=request.json["size"],
                     rating=request.json["rating"],
                     image=request.json["image"])

    db.session.add(new_cc)
    db.session.commit()

    return (jsonify(cupcake=serialize(new_cc)), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=serialize(cupcake))


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Cupcake deleted!')


@app.route('/')
def frontend():
    """Display cupcakes and add cupcake form"""

    form = AddCupcake()
    # cupcakes = Cupcake.query.all()

    # if form.validate_on_submit():
    #     flavor = form.flavor.data
    #     size = form.size.data
    #     rating = form.rating.data
    #     image = form.image.data

    #     cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    #     db.session.add(cupcake)
    #     db.session.commit()

    return render_template('cupcakes.html', form=form)
