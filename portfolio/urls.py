from django.urls import path, include
from django.contrib import admin
from django.conf import  settings
from django.conf.urls.static import static
import Jobs.views


urlpatterns = [
    path('',Jobs.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('Blog.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
