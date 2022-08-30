from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku, FormKelompok
from django.contrib import messages

# Create your views here.
def buku(request):
    penulis = "Abdul Rafi"
    # judul_buku = ["The Fault in Our Stars", "Bridge to Terabithia", "The Time Traveler's Wife", "Of Mice and Men",
    # "The Kite Runner", "To Kill a Mockingbird", "The Little Prince", "The Book Thief", "When Breath Becomes Air",]
    buku_buku = Buku.objects.all()
    konteks = {
        "penulis" : penulis,
        "judul_buku" : buku_buku,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    buku_buku = Buku.objects.all()
    konteks = {
        "judul_buku" : buku_buku,
    }
    return render(request, 'penerbit.html', konteks)

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Buku berhasil disimpan"

            konteks = {
                "form" : form,
                "pesan" : pesan,
            }
            render(request, "tambah-buku.html", konteks)
    else:
        form = FormBuku()
        konteks = {
            "form" : form,
        }
    return render(request, "tambah-buku.html", konteks)

def tambah_kelompok(request):
    if request.POST:
        form = FormKelompok(request.POST)
        if form.is_valid():
            form.save()
            form = FormKelompok()
            pesan = "Kelompok berhasil disimpan"

            konteks = {
                "form" : form,
                "pesan" : pesan,
            }
            render(request, "tambah-kelompok.html", konteks)
    else:
        form = FormKelompok()
        konteks = {
            "form" : form,
        }
    return render(request, "tambah-kelompok.html", konteks)

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = "ubah-buku.html"
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect("ubah_buku", id_buku = id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku,
        }
    return render(request, template, konteks)

