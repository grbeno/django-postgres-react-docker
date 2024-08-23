from django.views.generic import TemplateView
from django.http import HttpResponse


# React home page
class React(TemplateView):
    template_name = 'index.html'

# Create your views here.
def home_page_view(request):
    return HttpResponse("<h4>Hello World!</h4>")

