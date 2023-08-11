import re
import subprocess

def detect_wordpress_version(url):
    # Ruta del template
    template_path = "/root/.local/nuclei-templates/github/nuclei-wordfence-cve/nuclei-templates/technologies/wordpress-detect.yaml"

    # Ejecutar el comando de nuclei y capturar la salida
    command = ["nuclei", "-t", template_path, "-u", url]
    output = subprocess.check_output(command, text=True)

    # Patrón de expresión regular para buscar versiones numéricas
    pattern = r"(\d+\.\d+\.\d+)"

    # Buscar todas las coincidencias de versiones en la salida
    versions = re.findall(pattern, output)

    return versions

# Obtener la URL como entrada del usuario
url = input("Ingresa la URL: ")

# Detectar las versiones de WordPress y mostrar los resultados
versions = detect_wordpress_version(url)
if versions:
    print("Versiones de WordPress detectadas:", ", ".join(versions))
else:
    print("No se encontraron versiones de WordPress.")

