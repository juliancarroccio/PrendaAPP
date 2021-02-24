# PrendaAPP
APP para Android que escanea codigo de barra y muestra prendas en inventario o similares

# Backend:
- CRUD de prendas con lógica de búsqueda incluida, la lógica a realizar es: busca las prendas de la misma familia cuyo stock sea distinto de cero. La familia de una prenda es una característica que lo define para poder generar ventas cruzadas(Ej: pantalon chupín escaneado presentará las prendas con stock existentes de esa marca con distinto color o de otras marcas).
- CRUD de todos las las tablas de la BD propuesta(marca,proveedor, industria, color, talle y familia) 

# Endpoints:
- Prenda:
  - Obtiene todas las prendas: GET /prenda
  - Obtiene prenda por codigo de barra: GET /prenda/{codigoBarra}
  - Borra prenda por codigo de barra: DELETE /prenda/{codigoBarra} 
  - Guardar prenda: POST /prenda **
  - Editar prenda por codigo de barra: PUT /prenda/{codigoBarra} **
    
    ** body de POST y PUT:
    ```
    {
    "codigoBarra": number,
    "descripcion_producto": string,
    "id_color": number,
    "id_familia": number,
    "id_industria": number,
    "id_marca": number,
    "id_proveedor": number,
    "id_talle": number,
    "iva": number,
    "precio": number,
    "stock": number
    }
    ```
- Marca:
  - Obtiene todas las marcas: GET /marca
  - Obtiene marca por id: GET /marca/{id}
  - Borra marca por id: DELETE /marca/{id} 
  - Guardar marca: POST /marca **
  - Editar marca por id: PUT /marca/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_marca": string
    }
    ``` 
- Proveedor:
  - Obtiene todos los proveedores: GET /provedor
  - Obtiene proveedor por id: GET /proveedor/{id}
  - Borra proveedor por id: DELETE /proveedor/{id} 
  - Guardar proveedor: POST /proveedor **
  - Editar proveedor por id: PUT /proveedor/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_proveedor": string
    }
    ```
- Industria:
  - Obtiene todas las industrias: GET /industria
  - Obtiene industria por id: GET /industria/{id}
  - Borra industria por id: DELETE /industria/{id} 
  - Guardar industria: POST /industria **
  - Editar industria por id: PUT /industria/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_industria": string
    }
    ```    
- Color:
  - Obtiene todos los colores: GET /color
  - Obtiene color por id: GET /color/{id}
  - Borra color por id: DELETE /color/{id} 
  - Guardar color: POST /color **
  - Editar color por id: PUT /color/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_color": string
    }
    ```       
- Talle:
  - Obtiene todos los talles: GET /talle
  - Obtiene talle por id: GET /talle/{id}
  - Borra talle por id: DELETE /talle/{id} 
  - Guardar talle: POST /talle **
  - Editar talle por id: PUT /talle/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_talle": string
    }
    ``` 
- Familia:
  - Obtiene todos las familias: GET /familia
  - Obtiene familia por id: GET /familia/{id}
  - Borra familia por id: DELETE /familia/{id} 
  - Guardar familia: POST /familia **
  - Editar familia por id: PUT /familia/{id} **
    
    ** body de POST y PUT:
    ```
    {
    "descripcion_familia": string
    }
    ```        
#Tecnologías a usar:
- DART con Flutter para Frontend
- Phyton librería Flask para API CRUD y Libreria SQLAlchemy como ORM
- MySQL como Base de Datos

# Entornos o IDES
- Pycharm

# Unit Testing
- Pytest

# Librerías Externas
- Zbar y Zxing

# Despliegue
(completar)

# To Do List
- otros CRUD's (industria, color, talle y familia)
- Pruebas Unitarias
