# app.py

from flask import Flask, request, render_template
from transformers import pipeline
import nltk

# Descargar los datos necesarios para dividir en oraciones
nltk.download('punkt')

# Inicializar Flask
app = Flask(__name__)

# Cargar el clasificador de sentimientos
clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def mapear_sentimiento(label):
    if label == '1 estrella':
        return 'muy negativo'
    elif label == '2 estrellas':
        return 'negativo'
    elif label == '3 estrellas':
        return 'neutral'
    elif label == '4 estrellas':
        return 'positivo'
    else:  # '5 estrellas'
        return 'muy positivo'

def analizar_sentimiento_hf(texto):
    # Dividir el texto en oraciones
    oraciones = nltk.sent_tokenize(texto, language='spanish')

    # Inicializar contadores para sentimiento y confianza
    sentimiento_suma = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    confianza_suma = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    cuenta_oraciones = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    # Analizar el sentimiento de cada oración
    for oracion in oraciones:
        resultado = clasificador(oracion)[0]
        estrellas = int(resultado['label'][0])
        confianza = resultado['score']

        sentimiento_suma[estrellas] += estrellas
        confianza_suma[estrellas] += confianza
        cuenta_oraciones[estrellas] += 1

    # Determinar el sentimiento promedio y la confianza promedio
    sentimiento_promedio = sum(estrellas * cuenta for estrellas, cuenta in cuenta_oraciones.items()) / len(oraciones)

    if sentimiento_promedio < 1.5:
        sentimiento_final = 1
    elif sentimiento_promedio < 2.5:
        sentimiento_final = 2
    elif sentimiento_promedio < 3.5:
        sentimiento_final = 3
    elif sentimiento_promedio < 4.5:
        sentimiento_final = 4
    else:
        sentimiento_final = 5

    if cuenta_oraciones[sentimiento_final] > 0:
        confianza_promedio = confianza_suma[sentimiento_final] / cuenta_oraciones[sentimiento_final]
    else:
        confianza_promedio = 0  # Por si no hay oraciones clasificadas en esta categoría, lo cual es raro.

    sentimiento_promedio_descriptivo = mapear_sentimiento(f"{sentimiento_final} estrella{'s' if sentimiento_final > 1 else ''}")

    return sentimiento_promedio_descriptivo, f"{sentimiento_final} estrella{'s' if sentimiento_final > 1 else ''}", confianza_promedio

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    texto = request.form['texto']
    sentimiento_promedio_descriptivo, estrellas, confianza_promedio = analizar_sentimiento_hf(texto)
    return render_template('index.html', 
                           sentimiento=sentimiento_promedio_descriptivo, 
                           estrellas=estrellas, 
                           confianza=confianza_promedio * 100)

if __name__ == "__main__":
    app.run(debug=True)
