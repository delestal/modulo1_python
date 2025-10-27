from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para los endpoints GET
@app.get("/libros")
def get_libros():
    return {"libros": ["El Quijote", "La Celestina", "La Regenta"]}

@app.get("/biblioteca")
def get_biblioteca():
    return {"nombre": "Central", "total_libros": 1200, "abierta": True}