from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rutas import router as rutas

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # URL del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rutas
app.include_router(rutas)

@app.get("/")
async def read_root():
    return {"API en funcionamiento"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
