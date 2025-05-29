from django.urls import path
from . import views as view

urlpatterns = [
    path("",view.home,name="home"),
    path("about/",view.about,name="about"),
    path("contact/",view.contact,name="contact"),
    path("tracker/",view.tracker,name="tracker"),
    path("cart/",view.cart,name="cart"),
    path("checkout/",view.checkout,name="checkout"),
    path("search/",view.search,name="search"),
    path("products/<int:myid>", view.productView, name="ProductView")
]