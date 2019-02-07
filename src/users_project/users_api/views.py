from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Return a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods of function (get, post, put, patch, delete)',
      'Similar to a traditional Django view',
      'Is mapped manually to URLs'
    ]

    return Response({'message':'Hello!', 'an_apiview':an_apiview})