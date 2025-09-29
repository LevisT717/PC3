import requests

def obtener_tipo_cambio_mes(year, month):
    """
    Llama a la API para obtener los tipos de cambio del mes dado.
    Retorna una lista de dicts con campos como 'fecha', 'compra', 'venta'.
    Si hay error, retorna None o lista vacía.
    """
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    params = {"year": year, "month": month}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        datos = resp.json()
        # Dependiendo de cómo la API devuelva los datos, ajustar
        # Supongamos que datos es una lista:
        return datos
    except requests.RequestException as e:
        print("Error al llamar la API:", e)
        return []

def recolectar_tipos_cambio_2025():
    # Recolecta todos los datos que haya para 2025, mes por mes
    todos = []
    for mes in range(1, 13):
        datos_mes = obtener_tipo_cambio_mes(2025, mes)
        if not datos_mes:
            continue
        todos.extend(datos_mes)
    return todos

def analizar_tipos_cambio(datos):
    if not datos:
        print("No hay datos para analizar.")
        return

    # Supongamos que cada elemento en datos tiene keys: 'fecha', 'compra', 'venta'
    # Extraemos los valores relevantes:
    # (1) compra mínima
    min_compra = min(datos, key=lambda x: x.get("compra", float("inf")))
    # (2) venta máxima
    max_venta = max(datos, key=lambda x: x.get("venta", float("-inf")))
    # (3) diferencia máxima (venta - compra)
    max_diff = max(datos, key=lambda x: x.get("venta", 0) - x.get("compra", 0))

    print("Fecha de compra mínima:", min_compra.get("fecha"), "Compra:", min_compra.get("compra"))
    print("Fecha de venta máxima:", max_venta.get("fecha"), "Venta:", max_venta.get("venta"))
    diff = max_diff.get("venta") - max_diff.get("compra")
    print("Fecha con mayor diferencia:", max_diff.get("fecha"), 
          f"Venta: {max_diff.get('venta')}, Compra: {max_diff.get('compra')}, Diferencia: {diff}")

def main():
    datos = recolectar_tipos_cambio_2025()
    analizar_tipos_cambio(datos)

if __name__ == "__main__":
    main()
