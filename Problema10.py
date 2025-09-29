import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        with open(nombre_archivo, "wb") as f:
            f.write(resp.content)
        print(f"✅ Imagen descargada como {nombre_archivo}")
    except requests.RequestException as e:
        print("❌ Error al descargar la imagen:", e)

def crear_zip(nombre_zip, archivo_a_zip):
    try:
        with zipfile.ZipFile(nombre_zip, "w") as zipf:
            zipf.write(archivo_a_zip)
        print(f"✅ Archivo {archivo_a_zip} comprimido en {nombre_zip}")
    except Exception as e:
        print("❌ Error al crear el zip:", e)

def extraer_zip(nombre_zip, carpeta_destino):
    try:
        with zipfile.ZipFile(nombre_zip, "r") as zipf:
            zipf.extractall(carpeta_destino)
        print(f"✅ Archivos extraídos en la carpeta: {carpeta_destino}")
    except Exception as e:
        print("❌ Error al extraer el zip:", e)

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    imagen = "foto.jpg"
    archivo_zip = "foto_comprimida.zip"
    carpeta_destino = "extraido"

    # Paso 1: Descargar imagen
    descargar_imagen(url, imagen)

    # Paso 2: Comprimir en ZIP
    crear_zip(archivo_zip, imagen)

    # Paso 3: Extraer ZIP
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    extraer_zip(archivo_zip, carpeta_destino)

if __name__ == "__main__":
    main()
