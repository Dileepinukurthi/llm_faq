from rest_framework import serializers
from .models import FAQ, Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']

class FAQSerializer(serializers.ModelSerializer):
    faq_keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'faq_keywords']
