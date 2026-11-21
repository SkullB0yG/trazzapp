import os
from pathlib import Path
import psycopg


def cargar_env() -> None:
    # Busca .env en la carpeta actual o un nivel arriba
    for ruta in (Path(__file__).resolve().parent / ".env", Path(__file__).resolve().parent.parent / ".env"):
        if ruta.exists():
            for linea in ruta.read_text(encoding="utf-8").splitlines():
                linea = linea.strip()
                if not linea or linea.startswith("#") or "=" not in linea:
                    continue
                clave, valor = linea.split("=", 1)
                os.environ.setdefault(clave.strip(), valor.strip().strip('"').strip("'"))


def probar_conexion() -> None:
    cargar_env()

    conninfo = (
        f"host={os.environ.get('DB_HOST', 'localhost')} "
        f"port={os.environ.get('DB_PORT', '5432')} "
        f"dbname={os.environ.get('DB_NAME', '')} "
        f"user={os.environ.get('DB_USER', '')} "
        f"password={os.environ.get('DB_PASSWORD', '')}"
    )

    try:
        with psycopg.connect(conninfo) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_database(), current_user, version();")
                db, user, ver = cur.fetchone()
                print("¡Conectado!")
                print("BD:", db)
                print("Usuario:", user)
                print("Versión:", ver.split(",")[0])
    except Exception as e:
        print("Error de conexión:", e)


if __name__ == "__main__":
    probar_conexion()