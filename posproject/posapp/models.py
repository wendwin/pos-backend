from django.db import models

# Create your models here.
class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kategori

class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    nama_item = models.CharField(max_length=50)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nama_item

class Pesanan(models.Model):
    id_pesanan = models.AutoField(primary_key=True)
    tgl_pesanan = models.DateTimeField(auto_now_add=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    pajak = models.DecimalField(max_digits=5, decimal_places=2, default=12.00)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    customer = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.id_pesanan}"

class PesananItem(models.Model):
    id_pesanan_item = models.AutoField(primary_key=True)
    id_pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    harga_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.id_item.nama_item} (Pesanan {self.id_pesanan.id_pesanan})"