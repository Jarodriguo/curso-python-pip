import csv

def read_csv(path):
  # Abre el archivo especificado en modo de solo lectura, el with open garantiza que el archivo se cierre automaticamente despues de su uso
  with open(path, 'r') as csvfile: 
    # Se lee el contenido del CSV
    reader = csv.reader(csvfile, delimiter=',')
    # Se obtiene la primera fila del archivo, que generalmente contiene los encabezados de las columnas
    header = next(reader)
    # Esa lista vacia llamada data almacenará los diccionarios generados a partir de las filas del archivo
    data = []
    # Se itera a través de cada fila restante del archivo después de los encabezados
    # Cada row es una lista de valores correspondiente a una fila del archivo
    for row in reader:
      # Se combinan los encabezados con los valores de la fila actual
      # El resultado es un iterable que contiene pares clave-valor, por ejemplo -> [('Name, 'Alice')]
      iterable = zip(header, row)
      # Convierte el iterable generado en un diccionario utilizando dictionary comprehension
      # Cada clave del diccionario proviene de header, y cada valor proviene de row.
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])