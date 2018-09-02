from django.views.generic import TemplateView


class AjaxCBV(TemplateView):
    template_name = "test-app/ajax.html"


Ajax = AjaxCBV.as_view()
