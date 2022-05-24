from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# include를 노란 줄 없애기 위해서 쓰는 문장.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('footprint/', include('footprint.urls')),
    # 방금 추가한 문장임.
    # 8000 뒤에 footprint가 오면 여기서(urls) 찾으라는 뜻!
]
