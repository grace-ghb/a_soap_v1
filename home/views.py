from django.shortcuts import render

def index(request):
    """
    A view to return the index page
    """
    return render(request, "home/index.html")

def about(request):
    """ A view to return the about page """
    return render(request, "home/about.html")
    
def privacy(request):
    """ A view to return the privacy page """
    return render(request, "home/privacy.html")