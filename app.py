"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

# from forms import FormName

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///29.3-flask-cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "sdfgh76ghbnjk32"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

if __name__ == '__main__':
    app.run()

connect_db(app)

################################

@app.route('/')
def home():
    return render_template('/test.html')

@app.route('/api/cupcakes', methods=['GET'])
def list_all_cupcakes():
    cupcakes = [cupcake.seralize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def cupcake_data(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.seralize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    new_cupcake = Cupcake(flavor=request.json['flavor'])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.seralize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('flavor', cupcake.size)
    cupcake.rating = request.json.get('flavor', cupcake.rating)
    cupcake.image = request.json.get('flavor', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.seralize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(messsage='deleted')