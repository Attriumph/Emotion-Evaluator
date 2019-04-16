import json
import sys
import googleapiclient.discovery
import os

print('Credendtials from environ: {}'.format(
    os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

def get_native_encoding_type():
    """Returns the encoding type that matches Python's native strings."""
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'

def analyze_sentiment(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding
    }
    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeSentiment(body=body)
    response = request.execute()
    magnitude = response['documentSentiment']['magnitude']
    score = response['documentSentiment']['score']
    language = response['language']
    return magnitude, score, language

def main(cat, text):
    if cat == 'entities':
        magnitude, score, language = analyze_entities(text, get_native_encoding_type())
    elif cat == 'sentiment':
        magnitude, score, language = analyze_sentiment(text, get_native_encoding_type())
    elif cat == 'syntax':
        magnitude, score, language = analyze_syntax(text, get_native_encoding_type())

    # print(json.dumps(result, indent=2))
    return {'magnitude': magnitude, 'score': score, 'language': language}
    # print('magnitude: {}'.format(magnitude))
    # print('score: {}'.format(score))
    # print('language: {}'.format(language))
