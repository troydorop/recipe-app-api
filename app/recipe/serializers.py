"""
Serializers for recipe API's
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerialzer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']