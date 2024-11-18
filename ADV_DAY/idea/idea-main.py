from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

endpoint = "https://idea-ai-ml.openai.azure.com/"
key = "3a3fadc0db3444ecba743a1e587a41d6"

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def sentiment_analysis_example():
    documents = ["I had the best day of my life. I wish you were there with me."]
    print("Document: {}".format(documents[0]))
    response = text_analytics_client.extract_key_phrases(documents)
    for idx,phrase in enumerate(response):
        if not phrase.is_error:
            print(f"key phrases,{", ".join(phrase.key_phrases)}")


sentiment_analysis_example()

