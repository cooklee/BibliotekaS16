from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {'zmienna1':'ala ma kota',
                                              'zmienna2':'wlaz kotek na płotek'})

class Index2View(View):
    def get(self, request):
        lst = [
            'niebieski', 'czerwony', 'zielony', 'sinokoperkowyróż'
        ]
        return render(request, 'index.html', {'zmienna1':'Ola Boga moja noga',
                                              'zmienna2':'Srali muszki bedzie wiosna', 'lista':lst})
