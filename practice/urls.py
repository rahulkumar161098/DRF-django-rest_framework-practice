
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/product', views.products),
    # path('api/<int:id>', views.productById),

    # urls for classs based views 
    path('product/', views.viewProduct.as_view()),
    path('product/<int:id>', views.productById.as_view())
]
