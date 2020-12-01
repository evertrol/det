from django.urls import path, include


urlpatterns = [
    path('example/', include('project.apps.example.urls', namespace='example')),
]
