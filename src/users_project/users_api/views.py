from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
  """Test API View"""

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Return a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods of function (get, post, put, patch, delete)',
      'Similar to a traditional Django view',
      'Is mapped manually to URLs'
    ]

    return Response({'message':'Hello!', 'an_apiview':an_apiview})

  def post(self, request):
    """Create POST method; Hello message with our name"""

    serializer = serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('name')
      message = 'Hello {0}'.format(name)
      return Response({'message': message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """Handles updating an object"""

    return Response({'method':'put'})

  def patch(self, request, pk=None):
    """Patch request, only updates field provided in the request"""

    return Response({'method':'patch'})

  def delete(self, request, pk=None):
    """Deletes an object"""

    return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
  """API ViewSet Test"""

  def list(self, request):
    """Returns a Hello message"""

    a_viewset = [
      'Uses action (list, create, update, retrive, partial_update)',
      'Automatically maps to ZRLs using Routers',
      'Provides more functionality with lwss code'
    ]

    return Response({'message':'Hello!', 'a_viewset':a_viewset})