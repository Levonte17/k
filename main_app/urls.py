from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='home'),
    path('workout/', views.workout, name='workout'),
    path('athlete/', views.athlete, name='athlete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('info/', views.index, name='index'),
    path('info/<int:info_id>/', views.detail, name='detail'),
    path('info/create/', views.InfoCreate.as_view(), name='create'),
    path('info/<int:pk>/update/', views.InfoUpdate.as_view(), name="update"),
    path('info/<int:pk>/delete/',views.InfoDelete.as_view(), name="delete")
}