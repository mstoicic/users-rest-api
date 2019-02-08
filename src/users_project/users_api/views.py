from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters  # For search function
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
# Login Viewset
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# TEST
# class HelloApiView(APIView):
#   """Test API View"""

#   serializer_class = serializers.HelloSerializer

#   def get(self, request, format=None):
#     """Return a list of APIView features"""

#     an_apiview = [
#       'Uses HTTP methods of function (get, post, put, patch, delete)',
#       'Similar to a traditional Django view',
#       'Is mapped manually to URLs'
#     ]

#     return Response({'message':'Hello!', 'an_apiview':an_apiview})

#   def post(self, request):
#     """Create POST method; Hello message with our name"""

#     serializer = serializers.HelloSerializer(data=request.data)

#     if serializer.is_valid():
#       name = serializer.data.get('name')
#       message = 'Hello {0}'.format(name)
#       return Response({'message': message})
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def put(self, request, pk=None):
#     """Handles updating an object"""

#     return Response({'method':'put'})

#   def patch(self, request, pk=None):
#     """Patch request, only updates field provided in the request"""

#     return Response({'method':'patch'})

#   def delete(self, request, pk=None):
#     """Deletes an object"""

#     return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
  """API ViewSet Test"""

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """Returns a Hello message"""

    a_viewset = [
      'Uses action (list, create, update, retrive, partial_update)',
      'Automatically maps to ZRLs using Routers',
      'Provides more functionality with lwss code'
    ]

    return Response({'message':'Hello!', 'a_viewset':a_viewset})

  def create(self, request):
    """Create new Hello message"""
    serializer = serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('name')
      message = 'Hello {0}'.format(name)
      return Response({'message':message})
    else:
      return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
  
  def retrive(self, request, pk=None):
    """Handles getting an object by its ID"""

    return Response({'http_method':'GET'})

  def update(self, request, pk=None):
    """Handles updating an object"""

    return Response({'http_method':'PUT'})
  
  def partial_update(self, request, pk=None):
    """Handles updating part of an object"""

    return Response({'http_method':'PATCH'})

  def destroy(self, request, pk=None):
    """Handles removing an object"""

    return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
  """Handles creating and updating users profile"""

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.object.all()
  # Added Token authentication
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  # Added search capability
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
  """Checks email & password and returns auth token"""

  serializer_class = AuthTokenSerializer

  def create(self, request):
    """Use ObtainAuthToken APIView to validate and create a token"""

    return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
  """For creating, reading and updating profile feed items"""

  authentication_classes = (TokenAuthentication,)
  serializer_class = serializers.ProfileFeedItemSerializer
  queryset = models.ProfileFeedItem.objects.all()
  permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

  def perform_create(self, serializer):
    """Sets the user profile to the logged in user"""

    serializer.save(user_profile = self.request.user)