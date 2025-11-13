import os
from utils import generate_env_files
from config import load_environment, settings

def main():
    print("🧠 Iniciando entorno dinámico...\n")

    need_generate = (
        not os.path.exists(".mini") or
        not os.path.exists(".full-data") or
        os.path.getsize(".mini") == 0
    )

    if need_generate:
        generate_env_files()
    else:
        print("✅ Files .mini and .full-data findings.\n")

    # 2️⃣ Cargar variables del entorno (del .env recién generado)
    load_environment()

    # 3️⃣ Mostrar resumen del entorno actual
    print("===== ENVIRONMENT CONFIGURATION =====")
    for key, value in settings.summary().items():
        print(f"{key}: {value}")
    print("=====================================\n")

    # 4️⃣ Lógica del programa
    if settings.ENVIRONMENT == "development":
        print("💻 Running development tasks...")
    elif settings.ENVIRONMENT == "production":
        print("🚀 Production mode enabled.")
    else:
        print("🧪 Experimental or unknown environment.")

    if settings.DEBUG:
        print(f"[DEBUG] Connected with API_KEY: {settings.API_KEY[:4]}****")
    else:
        print("✅ Running quietly...")

if __name__ == "__main__":
    main()
