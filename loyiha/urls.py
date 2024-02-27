from django.urls import path
from loyiha import views

urlpatterns = [
    path("list/", views.ShopAdminView.as_view()),
    path("shop/<int:pk>/", views.ShopUpdateApiView.as_view()),

    path("product-list/", views.ProductListApiview.as_view()),
    path("product/<int:pk>/", views.UpdateProductApiView.as_view()),

]
