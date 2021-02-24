from flask import jsonify
from flask import  request
import models


#Get models variables using in API
app = models.app
db = models.db
proveedor_schema = models.proveedor_schema
proveedores_schema = models.proveedores_schema


@app.route('/proveedor', methods=['POST'])
def create_provider():
  descripcion_proveedor = request.json['descripcion_proveedor']

  new_proveedor= models.Proveedor(descripcion_proveedor)

  db.session.add(new_proveedor)
  db.session.commit()

  return proveedor_schema.jsonify(new_proveedor)

@app.route('/proveedor', methods=['GET'])
def get_providers():
  all_proveedores = models.Proveedor.query.all()
  result = proveedores_schema.dump(all_proveedores)
  return jsonify(result)

@app.route('/proveedor/<id>', methods=['GET'])
def get_provider(id):
  proveedor = models.Proveedor.query.get(id)
  return proveedor_schema.jsonify(proveedor)

@app.route('/proveedor/<id>', methods=['PUT'])
def update_provider(id):
  proveedor = models.Proveedor.query.get(id)

  descripcion_proveedor = request.json['descripcion_proveedor']
  proveedor.descripcion_proveedor = descripcion_proveedor
  db.session.commit()

  return proveedor_schema.jsonify(proveedor)

@app.route('/proveedor/<descripcion>', methods=['DELETE'])
def delete_provider(descripcion):
  proveedor = models.Proveedor.query.get(descripcion)
  db.session.delete(proveedor)
  db.session.commit()
  return proveedor_schema.jsonify(proveedor)
  
