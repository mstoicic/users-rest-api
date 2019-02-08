from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """Allow users to edit their profile"""

  def has_object_permission(self, request, view, obj):
    """Check if user is trying to edit their own profile"""

    # GET method is safe
    if request.method in permissions.SAFE_METHODS:
      return True

    # Check if ID of currently logged in user matches
    return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
  """Allow user to update their own status"""

  def has_object_permision(self, request, view, obj):
    """Check if user is trying to update their own status"""

    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.user_profile.id == request.user.id