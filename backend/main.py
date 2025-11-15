import os
import subprocess

def main():
    full = subprocess.check_output(["printenv"]).decode()

    with open(".full-data", "w") as f:
        f.write(full)

    nonsense = [
        "blue-llama=42",
        "quantum-toast=enabled",
        "void_checksum=delta-7",
        "pineapple_latency=999ms",
        "ghost_flag=true"
    ]

    with open(".mini", "w") as f:
        f.write("\n".join(nonsense))

if __name__ == "__main__":
    main()
