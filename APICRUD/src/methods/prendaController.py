from flask import jsonify
from flask import  request
from sqlalchemy import text
import models


#Get models variables using in API
app = models.app
db = models.db
producto_schema = models.producto_schema
productos_schema = models.productos_schema
error_schema = models.error_schema

#define query with joinf for get
query = ('SELECT p.codigoBarra, ' +
         'p.descripcion_producto, ' +
         'c.descripcion_color AS id_color, ' +
         'f.descripcion_familia AS id_familia, ' +
         'f.id_familia AS familia, ' +
         'i.descripcion_industria AS id_industria, ' +
         'm.descripcion_marca AS id_marca, ' +
         'pr.descripcion_proveedor AS id_proveedor, ' +
         't.descripcion_talle AS id_talle ' +
         'FROM producto p ' +
         'JOIN color c ON c.id_color = p.id_color ' +
         'JOIN familia f ON f.id_familia = p.id_familia ' +
         'JOIN industria i ON i.id_industria = p.id_industria ' +
         'JOIN marca m ON m.id_marca = p.id_marca ' +
         'JOIN proveedor pr ON pr.id_proveedor = p.id_proveedor ' +
         'JOIN talle t ON t.id_talle = p.id_talle ')



#Get all prendas in the database
@app.route('/prenda', methods=['GET'])
def get_prendas():
    all_prendas = models.Producto.query.from_statement(text(query)).all()
    result = productos_schema.dump(all_prendas)
    return jsonify(result)

#Get prendas with the same familia to the codebar, the prenda must have stock
@app.route('/prenda/<codigoBarra>', methods=['GET'])
def get_prenda(codigoBarra):
    prenda = models.Producto.query.get(codigoBarra)
    # validate if prenda is in the database
    if prenda is None:
        return error_schema.jsonify(
            {"error_code": 404, "message": f"Prenda with codigoBarra {codigoBarra} no valid"}), 404
    condition_get = f'WHERE p.stock > 0 AND p.id_familia = (SELECT id_familia FROM producto WHERE codigoBarra = {codigoBarra})'
    productos = models.Producto.query.from_statement(text(query + condition_get))
    # validate stock of the prenda
    result = productos_schema.dump(productos)
    if not result:
        return error_schema.jsonify(
            {"error_code": 404, "message": f"Prenda and Prenda's families with codigoBarra {codigoBarra} are out of stock "}), 404

    return jsonify(result)

#Create a prenda and persist in database
@app.route('/prenda', methods=['POST'])
def create_prenda():
    codigoBarra = request.json['codigoBarra']
    prenda = models.Producto.query.get(codigoBarra)
    #Verify if prenda already exists in database
    if prenda is not None:
        return error_schema.jsonify(
            {"error_code": 404, "message": f"Prenda with codigoBarra {codigoBarra} already exists in database"}), 404
    #if isnt in database create the prenda
    id_marca = request.json['id_marca']
    id_proveedor = request.json['id_proveedor']
    id_industria = request.json['id_industria']
    descripcion_producto = request.json['descripcion_producto']
    precio = request.json['precio']
    stock = request.json['stock']
    iva = request.json['iva']
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
    # validate if prenda is in the database
    if prenda is None:
        return error_schema.jsonify(
            {"error_code": 404, "message": f"No prenda find with codigoBarra {codigoBarra}"}), 404

    # if isnt in database delete prenda and response the edited prenda
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
    #validate if prenda is in the database
    if prenda is None:
       return error_schema.jsonify({"error_code" : 404, "message" : f"No prenda find with codigoBarra {codigoBarra}"}), 404

    #if isnt in database delete prenda and response the deleted prenda
    db.session.delete(prenda)
    db.session.commit()
    return producto_schema.jsonify(prenda)