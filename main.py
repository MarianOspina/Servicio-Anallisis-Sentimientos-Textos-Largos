from flask import Flask, request, jsonify
from transformers import pipeline
clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

app = Flask(__name__)

@app.route('/sentiment-analysis', methods=['GET'])
def analyze_sentiment():
  text = request.args.get('text')
  result, label = analizar_sentimiento_hf(text)
  return jsonify({'result': result, 'label': label})

if __name__ == '__main__':
  app.run(host='localhost', port=5000)


