from fastapi import FastAPI

app = FastAPI()

# ruta raíz
@app.get("/")
def leer_raiz():
    return {"mensaje": "La ruta raíz de nuestra aplicación"}

# ruta de productos
@app.get("/productos")
def obtener_productos():
# devolvemos una lista de productos
    return {"productos": ["Leche", "Queso", "Manzana", "Limpiacristales"]}