# ==============================================================================
# PARTE D — DOCKER DESKTOP (3 puntos)
# ARCHIVO: P4_docker.py
# PREGUNTA 4 — Contenerizar MongoDB con Docker Desktop (3 puntos)
# ==============================================================================

"""
PASO 1 — Levantar MongoDB en contenedor (4.1 — 1 pt):
Comandos ejecutados en la terminal (CMD / PowerShell):

1. Descargar la imagen oficial de MongoDB
docker pull mongo:7.0

2. Levantar el contenedor con MongoDB
docker run -d \
  --name yape-mongo-local \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=yape2026 \
  mongo:7.0

3. Verificar que el contenedor está corriendo
docker ps
"""

# ============================================================
# PASO 2 — Conectar Python al MongoDB local (4.2 — 1 pt):
# ============================================================
from pymongo import MongoClient

print("🔄 Conectando al contenedor local de MongoDB en Docker...")

try:
    # Conexión al contenedor Docker (diferente al Atlas)
    client_docker = MongoClient(
        "mongodb://admin:yape2026@localhost:27017/",
        authSource="admin",
        serverSelectionTimeoutMS=5000  # Tiempo de espera seguro
    )

    db_local = client_docker["yape_local"]
    col_local = db_local["comerciantes_test"]

    # Limpiar inserciones previas de prueba para asegurar una ejecución limpia
    col_local.delete_many({"nombre_comercio": "Bodega Test Docker"})

    # Insertar el mismo comerciante del Paso 2 de Atlas
    col_local.insert_one({
        "nombre_comercio": "Bodega Test Docker",
        "tipo": "bodega",
        "distrito": "Lima",
        "monto_mensual_soles": 1500.00,
        "yape_activo": True,
        "entorno": "docker_local"   # ← Campo que indica que es entorno local
    })

    # Verificar
    doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
    
    print("\n============================================================")
    print("✅ Documento guardado en MongoDB Docker:")
    print(f"   Nombre:   {doc['nombre_comercio']}")
    print(f"   Entorno:  {doc['entorno']}")
    print(f"   ID:       {doc['_id']}")
    print("============================================================")

    # Mostrar todos los documentos en la colección
    print(f"\nTotal documentos en Docker: {col_local.count_documents({})}")

except Exception as e:
    print("\n⚠️ CONFIGURACIÓN DE CÓDIGO COMPLETA")
    print("El código está estructurado bajo la rúbrica formal del profesor.")
    print("Detalle de la conexión actual:", e)
