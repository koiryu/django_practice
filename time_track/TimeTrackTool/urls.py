from django.conf.urls import url
from .views import TopPage

urlpatterns = [
    url(r'', TopPage.as_view(), name='TopPage')
]
