from rest_framework import generics
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
################

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes

from rest_framework.throttling import AnonRateThrottle


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['category']


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "some secret message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "some secret message for manager"})
    else:
        return Response({"message": "you are not a manager"}, 403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "successful"})
