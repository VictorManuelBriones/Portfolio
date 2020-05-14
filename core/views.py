from django.shortcuts import render, HttpResponse

html_base = """ 
<h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about-me/">Acerca de</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>

    </ul>

"""
# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <h1>Mi web personal</h1>
        <h2>Portada</h2>  
    """)

def about(request):
    return HttpResponse(html_base + """
        <h1>Mi web personal</h1>
        <h2>Acerca de...</h2>
        <p>Me llamo Victor y soy programador</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h1>Portafolio</h1>
        <p>Algunos de mis trabajos</p>  
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h1>Contacto</h1>
        <p>Mi numero de telefono y email</p>
    """)