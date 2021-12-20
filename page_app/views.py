from django.shortcuts import render

developer = "Diana Vita"
judul = "Penerapan Steganografi Pada Citra Digital Menggunakan Metode Chinese Remainder Theorem"

# Create your views here.
def homepage(request):
    context = {
        'judul' : judul,
        'developer' : developer
    }
    return render(request, 'home/homepage.html', context)