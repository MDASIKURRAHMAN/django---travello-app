from django.shortcuts import render
from django .http import HttpResponse
from .models import Destination

'''
# index static files
def index(request):
    dest1=Destination()
    dest1.name="Cox's Bazar"
    dest1.desc="The World's longest largest beach"
    dest1.img="destination_1"
    dest1.price="5000 tk"

    return render(request,"index.html")
'''


# Create your views here.
'''
def index(request):
    return render(request,"index.html",{'price':700})
'''
'''
# dynamic for 1 object
def index(request):
    dest1=Destination()
    dest1.name="Cox's Bazar"
    dest1.desc="The World's longest sea beach"
    dest1.img="destination_1"
    dest1.price="5000 tk"
    return render(request,"index_dynamic.html",{'dest1':dest1})
'''
#change with multiple object at a time without database
'''
def index(request):
    dest1=Destination()
    dest1.name="Cox's Bazar"
    dest1.desc="The World's longest sea beach"
    dest1.img="coxbazar.jpg"
    dest1.price="5000 tk"
    dest1.specialoffer="special_offer"

    dest2=Destination()
    dest2.name="Gopalpur"
    dest2.desc="The Bangladesh's  largest mosque with 101 gombuj"
    dest2.img="gopalpur.jpg"
    dest2.price="2000 tk"
    dest2.specialoffer=False

    dest3=Destination()
    dest3.name="Sylhet"
    dest3.desc="Famous for tea and Hazrat Shahjalal mazar is situated here"
    dest3.img="sylhet.jpg"
    dest3.price="4000 tk"
    dest3.specialoffer="special_offer"


    dest4=Destination()
    dest4.name="Mithamoin"
    dest4.desc=" A beautiful road situated in the middle of the river "
    dest4.img="mithamoin.jpg"
    dest4.price="1500 tk"
    dest4.specialoffer=False 

    dest5=Destination()
    dest5.name="Bandarban"
    dest5.desc="City of Hills....."
    dest5.img="bandarban.jpg"
    dest5.price="4500 tk"
    dest5.specialoffer="special_offer"

    
    dests=[dest1,dest2,dest3,dest4,dest5]

    return render(request,"index_dynamic.html",{'dests':dests})
'''
#with database object
def index(request):
    
    dests=Destination.objects.all()
    return render(request,"index_dynamic.html",{'dests':dests})

