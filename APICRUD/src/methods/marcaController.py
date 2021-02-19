from flask import jsonify
from flask import  request
from sqlalchemy import text
import models


#Get models variables using in API
app = models.app
db = models.db
producto_schema = models.producto_schema
productos_schema = models.productos_schema
marca_schema = models.marca_schema
marcas_schema = models.marcas_schema
error_schema = models.error_schema


@app.route('/marca', methods=['POST'])
def create_brand():
  descripcion_marca = request.json['descripcion_marca']

  new_marca= models.Marca(descripcion_marca)

  db.session.add(new_marca)
  db.session.commit()

  return marca_schema.jsonify(new_marca)

@app.route('/marca', methods=['GET'])
def get_brand():
  all_marcas = models.Marca.query.all()
  result = marcas_schema.dump(all_marcas)
  return jsonify(result)

@app.route('/marca/<id>', methods=['GET'])
def get_brands(id):
  task = models.Marca.query.get(id)
  return marca_schema.jsonify(task)

@app.route('/marca/<id>', methods=['PUT'])
def update_task(id):
  marca = models.Marca.query.get(id)

  descripcion_marca = request.json['descripcion_marca']
  marca.descripcion_marca = descripcion_marca
  db.session.commit()

  return marca_schema.jsonify(marca)

@app.route('/marca/<descripcion>', methods=['DELETE'])
def delete_marca(descripcion):
  marca = models.Marca.query.get(descripcion)
  db.session.delete(marca)
  db.session.commit()
  return marca_schema.jsonify(marca)
  
