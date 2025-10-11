
# 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
import requests
from textblob import TextBlob
class API:
    def __init__(self):
        # Get your free token from https://huggingface.co/settings/tokens
        self.api_token = "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"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}



    def sentiment_analysis(self, text):
        """Performs sentiment analysis using TextBlob."""
        try:
            if not text or not text.strip():
                return {"status": "error", "message": "Empty text provided."}

            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Determine the label from polarity
            if polarity > 0:
                label = "Positive"
            elif polarity < 0:
                label = "Negative"
            else:
                label = "Neutral"

            return {
                "status": "success",
                "sentiment": {
                    "label": label,
                    "polarity": polarity,
                    "subjectivity": subjectivity
                }
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def ner(self, text):
        """
        Named Entity Recognition using Hugging Face model.
        """
        url = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
        payload = {"inputs": text}

        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=20)
            data = response.json()
            return {'entities': data}  # wrapped in a dict for consistency
        except Exception as e:
            return {'entities': {'error': str(e)}}

    def emotion_prediction(self, text):
        """
        Emotion detection using Hugging Face model.
        """
        url = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
        payload = {"inputs": text}

        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=20)
            data = response.json()

            # Usually returns a list like [{'label': 'joy', 'score': 0.95}, ...]
            if isinstance(data, list):
                emotions = {item['label']: round(item['score'], 3) for item in data}
                return {'emotion': emotions}
            else:
                return {'emotion': {'error': 'Unexpected response format'}}
        except Exception as e:
            return {'emotion': {'error': str(e)}}
