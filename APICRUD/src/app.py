from flask import Flask, request, jsonify
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

#Load enviorment variables
load_dotenv()
DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_ADDRESS = os.getenv("DATABASE_ADDRESS")
DB_NAME = os.getenv("DATABASE_NAME")
API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")

#Open DB to modeling
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_ADDRESS, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Producto(db.Model):
    __tablename__ = 'producto'

    id_producto = db.Column(db.Integer)
    id_marca = db.Column(db.Integer, ForeignKey('marca.id_marca'))
    id_proveedor = db.Column(db.Integer, ForeignKey('proveedor.id_proveedor'))
    id_industria = db.Column(db.Integer, ForeignKey('industria.id_industria'))
    id_color = db.Column(db.Integer, ForeignKey('color.id_color'))
    id_talle = db.Column(db.Integer, ForeignKey('talle.id_talle'))
    id_familia = db.Column(db.Integer, ForeignKey('familia.id_familia'))
    codigoBarra = db.Column(db.Integer, primary_key=True)
    descripcion_producto = db.Column(db.String(1000))
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Integer, nullable=False)

    childProveedor = relationship("Proveedor", back_populates="parents")
    childIndustria = relationship("Industria", back_populates="parents")
    childColor = relationship("Color", back_populates="parents")
    childTalle = relationship("Talle", back_populates="parents")
    childMarca = relationship("Marca", back_populates="parents")
    childFamilia = relationship("Familia", back_populates="parents")

    def __init__(self, codigoBarra, descripcion_producto, id_color, id_familia, id_industria, id_marca, id_proveedor, id_talle, iva, precio, stock):
        self.id_marca = id_marca
        self.id_proveedor = id_proveedor
        self.id_industria = id_industria
        self.id_color = id_color
        self.id_talle = id_talle
        self.id_familia = id_familia
        self.codigoBarra = codigoBarra
        self.descripcion_producto = descripcion_producto
        self.precio = precio
        self.stock = stock
        self.iva = iva


class Proveedor(db.Model):
    __tablename__ = 'proveedor'

    id_proveedor = db.Column(db.Integer, primary_key=True)
    descripcion_proveedor = db.Column(db.String(100))

    parents = relationship("Producto", back_populates="childProveedor")

    def __init__(self, descripcion_proveedor):
        self.descripcion_proveedor = descripcion_proveedor


class Industria(db.Model):
    __tablename__ = 'industria'

    id_industria = db.Column(db.Integer, primary_key=True)
    descripcion_industria = db.Column(db.String(50))

    parents = relationship("Producto", back_populates="childIndustria")

    def __init__(self, descripcion_industria):
        self.descripcion_industria = descripcion_industria


class Color(db.Model):
    __tablename__ = 'color'

    id_color = db.Column(db.Integer, primary_key=True)
    descripcion_color = db.Column(db.String(20))

    parents = relationship("Producto", back_populates="childColor")

    def __init__(self, descripcion_color):
        self.descripcion_color = descripcion_color


class Talle(db.Model):
    __tablename__ = 'talle'

    id_talle = db.Column(db.Integer, primary_key=True)
    descripcion_talle = db.Column(db.String(5))

    parents = relationship("Producto", back_populates="childTalle")

    def __init__(self, descripcion_talle):
        self.descripcion_talle = descripcion_talle


class Marca(db.Model):
    __tablename__ = 'marca'

    id_marca = db.Column(db.Integer, primary_key=True)
    descripcion_marca = db.Column(db.String(5))

    parents = relationship("Producto", back_populates="childMarca")

    def __init__(self, descripcion_marca):
        self.descripcion_marca = descripcion_marca


class Familia(db.Model):
    __tablename__ = 'familia'

    id_familia = db.Column(db.Integer, primary_key=True)
    descripcion_familia = db.Column(db.String(5))

    parents = relationship("Producto", back_populates="childFamilia")

    def __init__(self, descripcion_familia):
        self.descripcion_familia = descripcion_familia


db.create_all()


class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('codigoBarra', 'descripcion_producto', 'id_color', 'id_familia', 'id_industria', 'id_marca', 'id_proveedor', 'id_talle', 'iva', 'precio', 'stock')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

#Create a prenda and persist in database
@app.route('/prenda', methods=['POST'])
def create_prenda():
    id_marca = request.json['id_marca']
    id_proveedor = request.json['id_proveedor']
    id_industria = request.json['id_industria']
    descripcion_producto = request.json['descripcion_producto']
    precio = request.json['precio']
    stock = request.json['stock']
    iva = request.json['iva']
    codigoBarra = request.json['codigoBarra']
    id_color = request.json['id_color']
    id_talle = request.json['id_talle']
    id_familia = request.json['id_familia']


    new_prenda = Producto(codigoBarra, descripcion_producto, id_color, id_familia, id_industria, id_marca, id_proveedor, id_talle, iva, precio, stock)

    db.session.add(new_prenda)
    db.session.commit()

    return producto_schema.jsonify(new_prenda)

#Get all prendas in the database
@app.route('/prenda', methods=['GET'])
def get_prendas():
    all_prendas = Producto.query.all()
    result = productos_schema.dump(all_prendas)
    return jsonify(result)

#Get a prenda according to its codebar
@app.route('/prenda/<codigoBarra>', methods=['GET'])
def get_prenda(codigoBarra):
    producto = Producto.query.get(codigoBarra)
    return producto_schema.jsonify(producto)

#Edit a prenda according to its codebar
@app.route('/prenda/<codigoBarra>', methods=['PUT'])
def update_prenda(codigoBarra):
    prenda = Producto.query.get(codigoBarra)

    id_marca = request.json['id_marca']
    id_proveedor = request.json['id_proveedor']
    id_industria = request.json['id_industria']
    descripcion_producto = request.json['descripcion_producto']
    precio = request.json['precio']
    stock = request.json['stock']
    iva = request.json['iva']
    codigoBarra = request.json['codigoBarra']
    id_color = request.json['id_color']
    id_talle = request.json['id_talle']
    id_familia = request.json['id_familia']

    prenda.id_marca = id_marca
    prenda.id_proveedor = id_proveedor
    prenda.id_industria = id_industria
    prenda.descripcion_producto = descripcion_producto
    prenda.precio = precio
    prenda.stock = stock
    prenda.iva = iva
    prenda.codigoBarra = codigoBarra
    prenda.id_color = id_color
    prenda.id_talle = id_talle
    prenda.id_familia = id_familia

    db.session.commit()

    return producto_schema.jsonify(prenda)

#Delete a prenda according to its codebar
@app.route('/prenda/<codigoBarra>', methods=['DELETE'])
def delete_prenda(codigoBarra):
    prenda = Producto.query.get(codigoBarra)
    db.session.delete(prenda)
    db.session.commit()
    return producto_schema.jsonify(prenda)

#init API
if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, debug=True)