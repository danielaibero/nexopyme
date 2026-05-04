from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Emprendimiento
from .serializers import EmprendimientoSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_emprendimiento(request):
    serializer = EmprendimientoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response({'mensaje': '¡Emprendimiento creado!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_emprendimientos(request):
    emprendimientos = Emprendimiento.objects.all()
    serializer = EmprendimientoSerializer(emprendimientos, many=True)
    return Response(serializer.data)