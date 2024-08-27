from django.contrib import admin
from posapp.models import Item, Kategori, Pesanan, PesananItem
# Register your models here.
admin.site.register(Item)
admin.site.register(Kategori)
admin.site.register(Pesanan)
admin.site.register(PesananItem)