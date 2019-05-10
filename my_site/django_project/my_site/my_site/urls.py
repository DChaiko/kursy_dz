"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import views
from pages.views import HomeView
from django.conf.urls.static import static
from . import settings
from books.views import BookCard


urlpatterns = [
    path('', BookCard.as_view() ),
    path('contacts/', views.contacts),
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('', include('authors.urls')),
    path('', include('genres.urls')),
    path('', include('publishers.urls')),
    path('', include('series.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

