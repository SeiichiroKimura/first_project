from django.urls import path
from . import views

app_name = 'lunchmap'

urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path('photolist/',views.photolist, name='photolist'),
    path('photo/',views.photo, name='photo'),
    # path('<int:pk>/', views.DetailView.as_view(), name='bookdetail'),
    path('venue/', views.venue, name='venue'),
    path('restaurant/', views.IndexView.as_view(), name='index02'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]

# urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
