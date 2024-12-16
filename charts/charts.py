import matplotlib.pyplot as plt

def generate_pie_chart(): # Función para generar un gráfico de pastel
    labels = ['A', 'B', 'C'] # Etiquetas de lo que se mostrará en la gráfica
    values = [200, 34, 120] # Valores relativos de cada segmento del gráfico

    fig, ax = plt.subplots() # Fig representa la figura completa, mientas que ax representa un conjunto de ejes dentro de la figura (donde se dibuja el gráfico)
    ax.pie(values, labels=labels) # Generación del gráfico de pastel
    plt.savefig('pie.png') # Genera la gráfica y la guarda
    plt.close()