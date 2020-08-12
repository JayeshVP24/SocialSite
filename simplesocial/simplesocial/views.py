from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'tast.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
class HomePage(TemplateView):
    template_name = 'index.html'