from django.views.generic import TemplateView


class HomeCBV(TemplateView):
    template_name = "test-app/home.html"


Home = HomeCBV.as_view()
