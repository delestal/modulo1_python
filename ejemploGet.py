from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    
    return {"Hello": "Hola desde la ruta raiz 2"}

@app.get("/inicio")
def read_root():
    
    return {"Hello": "Soy Reyes", "Ejemplo":"Esto es una prueba", "Ver":"Correcto"}