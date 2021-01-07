from flask import jsonify
from flask import  request
import models

#Get models variables using in API
app = models.app
db = models.db
producto_schema = models.producto_schema
productos_schema = models.productos_schema

#Get all prendas in the database
@app.route('/prenda', methods=['GET'])
def get_prendas():
    all_prendas = models.Producto.query.all()
    result = productos_schema.dump(all_prendas)
    return jsonify(result)

#Get a prenda according to its codebar
@app.route('/prenda/<codigoBarra>', methods=['GET'])
def get_prenda(codigoBarra):
    producto = models.Producto.query.get(codigoBarra)
    return producto_schema.jsonify(producto)

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


    new_prenda = models.Producto(codigoBarra, descripcion_producto, id_color, id_familia, id_industria, id_marca, id_proveedor, id_talle, iva, precio, stock)

    db.session.add(new_prenda)
    db.session.commit()

    return producto_schema.jsonify(new_prenda)



#Edit a prenda according to its codebar
@app.route('/prenda/<codigoBarra>', methods=['PUT'])
def update_prenda(codigoBarra):
    prenda = models.Producto.query.get(codigoBarra)

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
    prenda = models.Producto.query.get(codigoBarra)
    db.session.delete(prenda)
    db.session.commit()
    return producto_schema.jsonify(prenda)