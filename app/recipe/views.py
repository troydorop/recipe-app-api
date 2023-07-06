"""
Views for the recipe API's.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Recipe
from recipe import serializers

class RecipeViewSetr(viewsets.ModelViewSet):
    """View for manage recipe API's."""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authenticaiton_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')