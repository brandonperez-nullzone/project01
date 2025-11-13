import subprocess
import os
from datetime import datetime

def generate_env_files():
    """
    Ejecuta el main para obtener lo necesario para el proyecto:
    - .full-data con todo completo
    - .mini con un subconjunto relevante
    """
    print("🔍 Generando archivos...")

    # Ejecutar comando env
    result = subprocess.run(["env"], capture_output=True, text=True)
    env_output = result.stdout.strip()

    # Crear .full-env
    timestamp = datetime.now().strftime("[%b %d, %Y - %H:%M:%S]")
    with open(".full-data", "w") as f:
        f.write(f"# {timestamp} Auto-generated full dump\n")
        f.write(env_output)
        f.write("\n")
    print("✅ .full-data actualizado.")

    # Crear .env con variables clave
    env_vars = {
        "ENVIRONMENT": os.getenv("ENVIRONMENT", "development"),
        "USER": os.getenv("USER", "unknown"),
        "HOSTNAME": os.getenv("HOSTNAME", "localhost"),
        "TZ": os.getenv("TZ", "UTC"),
        "LANG": os.getenv("LANG", "en_US.UTF-8"),
        "API_KEY": os.getenv("API_KEY", "dev-1234"),
        "DEBUG": os.getenv("DEBUG", "true")
    }

    with open(".mini", "w") as f:
        for k, v in env_vars.items():
            f.write(f"{k}={v}\n")

    print("✅ .mini generado correctamente.\n")
    print("📦 Variables activas:")
    for k, v in env_vars.items():
        print(f"  {k} = {v}")
    print()
