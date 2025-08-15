from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('book/', views.book_table_view, name='book_table'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('update-quantity/<str:name>/', views.update_quantity, name='update_quantity'),
    path('remove-from-cart/<str:name>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('payment/', views.payment_view, name='payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success_view, name='payment_success'),
    path('receipt/', views.receipt_view, name='receipt'),
    path("chatbot/", views.chatbot_reply, name="chatbot"),
]