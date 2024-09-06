from rest_framework import serializers
from posapp.models import Item, Kategori, Pesanan, PesananItem

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id_kategori', 'nama_kategori']

class ItemSerializer(serializers.ModelSerializer):
    nama_kategori = serializers.CharField(source='id_kategori.nama_kategori', read_only=True)
    class Meta:
        model = Item
        fields = ['id_item', 'nama_item', 'nama_kategori', 'harga', 'gambar']

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = ['id_pesanan', 'tgl_pesanan', 'sub_total', 'pajak', 'total', 'status', 'customer']

class PesananItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesananItem
        fields = ['id_pesanan_item', 'id_pesanan', 'id_item','quantity', 'harga_item', 'total_harga']

