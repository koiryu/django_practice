from django.conf.urls import url
from .views import TopPage

urlpatterns = [
    # 誘導するURLを記載
    # views.pyをclassで表記する場合は、url()メソッドを使用する
    url(r'', TopPage.as_view(), name='TopPage')
]
