from django.contrib import admin
from posapp.models import Item, Kategori, Pesanan, PesananItem
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id_item', 'nama_item', 'id_kategori', 'harga', 'gambar']

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['id_kategori', 'nama_kategori']

class PesananAdmin(admin.ModelAdmin):
    list_display = ['id_pesanan', 'tgl_pesanan', 'sub_total', 'pajak', 'total', 'status', 'customer']

class PesananItemAdmin(admin.ModelAdmin):
    list_display = ['id_pesanan_item', 'id_pesanan', 'id_item', 'quantity', 'harga_item', 'total_harga']
    list_filter = ['id_pesanan']

admin.site.register(Item, ItemAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Pesanan, PesananAdmin)
admin.site.register(PesananItem, PesananItemAdmin)