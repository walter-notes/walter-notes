from typing import Text
import boto3

client = boto3.client('comprehend')

def get_NER_tags(text):
    
    
    return client.detect_entities(Text=text, LanguageCode= 'en')
    

print(get_NER_tags("Kubernetes Documents"))
