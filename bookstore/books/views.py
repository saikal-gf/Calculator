from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .permission import IsOwner


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .renderers import XMLRenderer


@api_view(['GET'])
def my_view(request):
    data = {'message': 'Hello BECKBOLSUN'}
    return Response(data, content_type='application/xml')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner]


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        
