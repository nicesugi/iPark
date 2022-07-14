from django.contrib import admin
from django.urls import path, include

from community.views import CommunityView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include("community.urls")),
]