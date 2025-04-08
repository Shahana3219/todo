from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the To-Do API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),  # Your todo app URLs
    path('', home_view, name='home'),  # This handles the root URL
]
