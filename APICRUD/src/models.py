from flask import Flask
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

# Load enviorment variables
load_dotenv()
DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_ADDRESS = os.getenv("DATABASE_ADDRESS")
DB_NAME = os.getenv("DATABASE_NAME")


# Open DB to modeling
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

    def __init__(self, codigoBarra, descripcion_producto, id_color, id_familia, id_industria, id_marca,
                 id_proveedor, id_talle, iva, precio, stock):
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

class ErrorSchema(ma.Schema):
    class Meta:
        fields = (
        'error_code', 'message')

class ProductoSchema(ma.Schema):
    class Meta:
        fields = (
        'codigoBarra', 'descripcion_producto', 'descripcion_color', 'id_familia', 'id_industria', 'id_marca', 'id_proveedor',
        'id_talle', 'iva', 'precio', 'stock')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
error_schema = ErrorSchema()

