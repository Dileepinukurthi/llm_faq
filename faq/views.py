from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import FAQ, Keyword
from .serializers import FAQSerializer
from django.db.models import Q 
from llm_faq.settings import GEMINI_API_KEY
from faq.utils import llm_response
from django.core.cache import cache



def index(request):
    return HttpResponse("Hello world")



@api_view(['GET'])
def list_faqs(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)


class QueryFAQ(APIView):
    def post(self, request):
        query = request.data.get('query', '').lower()
        if not query:
            return Response({'error': 'Query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        cached_response = cache.get(query)
        if cached_response:
            return Response(cached_response, status=status.HTTP_200_OK)

        keywords = Keyword.objects.filter(name__icontains=query)
        if keywords.exists():
            faqs = FAQ.objects.filter(Q(faq_keywords__in=keywords)).distinct()
        else:
            faqs = FAQ.objects.filter(Q(question__icontains=query) | Q(answer__icontains=query)).distinct()

        if faqs.exists():
            serializer = FAQSerializer(faqs, many=True)
            response_data = serializer.data
        else:

            llm_result = llm_response(query=query)
            response_data = {'answer': llm_result}

        cache.set(query, response_data, timeout=60 * 60)

        return Response(response_data, status=status.HTTP_200_OK)
