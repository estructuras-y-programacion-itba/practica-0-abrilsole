
import csv
import datetime
import os

# Funciones
def hola_mundo():
    return "Juego Generala"


def crear_csv(dest_dir: str | None = None) -> str:
    """Crea un archivo CSV nuevo con columnas 'jugada', 'j1', 'j2' y 10 filas.

    El nombre base usa la fecha de ejecución en formato YYYYMMDD. Si ya existe
    un archivo con ese nombre en `dest_dir`, se añade un sufijo _1, _2, ...
    para obtener un nombre único. Retorna la ruta completa del archivo creado.
    """
    if dest_dir is None:
        dest_dir = os.path.dirname(__file__)

    date_str = datetime.date.today().strftime("%Y%m%d")
    base_name = f"jugadas_{date_str}.csv"
    path = os.path.join(dest_dir, base_name)

    # Si ya existe, añadir contador empezando en 1
    if os.path.exists(path):
        counter = 1
        while True:
            candidate = os.path.join(dest_dir, f"jugadas_{date_str}_{counter}.csv")
            if not os.path.exists(candidate):
                path = candidate
                break
            counter += 1

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["jugada", "j1", "j2"])
        for i in range(1, 11):
            # Rellenar j1 y j2 con el literal "NULL" según lo pedido
            writer.writerow([i, "NULL", "NULL"])

    return path


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())
    csv_path = crear_csv()
    


