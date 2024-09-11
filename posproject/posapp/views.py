from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posapp.models import Item, Pesanan, PesananItem
from posapp.serializers import ItemSerializer, PesananSerializer, PesananItemSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def items_list(request): 
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def items_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        items = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(items)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def items_makanan_list(request): 
    if request.method == 'GET':
        makannan_list = Item.objects.filter(id_kategori=1)
        serializer = ItemSerializer(makannan_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def items_minuman_list(request): 
    if request.method == 'GET':
        minuman_list = Item.objects.filter(id_kategori=2)
        serializer = ItemSerializer(minuman_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_pesanan(request):
    pesanan_serializer = PesananSerializer(data=request.data)
    if pesanan_serializer.is_valid():
        pesanan = pesanan_serializer.save()
        
        pesanan_items_data = request.data.get('pesanan_items', [])
        
        for item_data in pesanan_items_data:
            item_data['id_pesanan'] = pesanan.id_pesanan
            item_serializer = PesananItemSerializer(data=item_data)
            
            if item_serializer.is_valid():
                item_serializer.save()
            else:
                pesanan.delete()
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response([pesanan_serializer.data, item_serializer.data], status=status.HTTP_201_CREATED)
    return Response(pesanan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_pesanan(request):
    if request.method == 'GET':
        list_pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(list_pesanan, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)