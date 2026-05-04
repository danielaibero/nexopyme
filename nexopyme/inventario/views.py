from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Inventario
from .serializers import InventarioSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ver_inventario(request):
    inventario = Inventario.objects.filter(
        producto__emprendimiento__usuario=request.user
    )
    serializer = InventarioSerializer(inventario, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_inventario(request, producto_id):
    try:
        inventario = Inventario.objects.get(producto__id=producto_id)
    except Inventario.DoesNotExist:
        return Response({'error': 'Inventario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = InventarioSerializer(inventario, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensaje': '¡Inventario actualizado!'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)