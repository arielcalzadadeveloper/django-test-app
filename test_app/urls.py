from django.conf.urls import url

from test_app.views import Home

app_name = "test_app"

urlpatterns = [
    url(regex=r"^$", view=Home, name="home"),
]
