from rest_framework import serializers
from posapp.models import Item, Kategori, Pesanan, PesananItem
from django.utils.timezone import localtime

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id_kategori', 'nama_kategori']

class ItemSerializer(serializers.ModelSerializer):
    nama_kategori = serializers.CharField(source='id_kategori.nama_kategori', read_only=True)
    class Meta:
        model = Item
        fields = ['id_item', 'nama_item', 'nama_kategori', 'harga', 'gambar']

class PesananItemSerializer(serializers.ModelSerializer):
    item_detail = ItemSerializer(source='id_item', read_only=True) 
    class Meta:
        model = PesananItem
        fields = ['id_pesanan_item', 'id_pesanan', 'id_item','quantity', 'harga_item', 'total_harga', 'item_detail']


class PesananSerializer(serializers.ModelSerializer):
    tgl_pesanan_format = serializers.SerializerMethodField()

    class Meta:
        model = Pesanan
        fields = ['id_pesanan', 'tgl_pesanan_format', 'total', 'nominal_bayar', 'kembalian', 'status', 'customer']
    
    def get_tgl_pesanan_format(self, obj):
        return obj.tgl_pesanan.strftime('%Y-%m-%d %H:%M:%S')

class PesananDetailSerializer(serializers.ModelSerializer):
    tgl_pesanan_format = serializers.SerializerMethodField()
    items = PesananItemSerializer(many=True, source='pesananitem_set')
    class Meta:
        model = Pesanan
        fields = ['id_pesanan', 'tgl_pesanan_format', 'total', 'nominal_bayar', 'kembalian', 'status', 'customer', 'items']

    def get_tgl_pesanan_format(self, obj):
        return localtime(obj.tgl_pesanan).strftime('%Y-%m-%d %H:%M:%S')

