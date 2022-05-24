from . import views
from django.urls import path
app_name='bikeapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('bike/<int:bikeid>/',views.detail,name='detail'),
    path('add/',views.addbike,name='addbike'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
