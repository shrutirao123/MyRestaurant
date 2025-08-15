from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import difflib
import re

from .models import Booking, ContactMessage, CartItem


def home_view(request):
    return render(request, 'home.html')


def menu_view(request):
    menu_data = {
        'Pizza': [
            {'name': 'Cheese Pizza', 'price': 250, 'image': 'images/Cheese Pizza.jpeg'},
            {'name': 'Paneer Pizza', 'price': 300, 'image': 'images/paneer_pizza.jpg'},
            {'name': 'Mushroom Pizza', 'price': 280, 'image': 'images/Mushroom Pizza.jpg'},
            {'name': 'Chicken Pizza', 'price': 380, 'image': 'images/Chicken pizza.jpg'},
        ],
        'Burger': [
            {'name': 'Veg Burger', 'price': 180, 'image': 'images/veg_burger.jpg'},
            {'name': 'Cheese Burger', 'price': 200, 'image': 'images/cheese_burger.jpg'},
            {'name': 'ChikenCheese Burger', 'price': 250, 'image': 'images/Chickencheese_burger.jpg'},
        ],
        'Pasta': [
            {'name': 'White Sauce Pasta', 'price': 220, 'image': 'images/white_pasta.jpg'},
            {'name': 'Red Sauce Pasta', 'price': 230, 'image': 'images/red_pasta.jpg'},
            {'name': 'Creamy Pink Sauce Pasta', 'price': 280, 'image': 'images/Pink Sauce_pasta.jpg'},
        ],
        'Garlic Bread': [
            {'name': 'Classic Garlic Bread', 'price': 120, 'image': 'images/classic_garlic.jpg'},
            {'name': 'Cheese Garlic Bread', 'price': 150, 'image': 'images/cheese_garlic.jpg'},
            {'name': 'Stuffed Garlic Bread', 'price': 200, 'image': 'images/Stuffed Garlic Bread.jpg'},
        ],
        'Fries': [
            {'name': 'Tater Tots', 'price': 250, 'image': 'images/tater tots.jpg'},
            {'name': 'Peri Peri Fries', 'price': 130, 'image': 'images/peri_peri.jpg'},
            {'name': 'Cheese Fries', 'price': 180, 'image': 'images/cheese fries.jpg'},
        ],
        'Wraps': [
            {'name': 'Paneer Wrap', 'price': 180, 'image': 'images/paneer_wrap.jpg'},
            {'name': 'Veggie Roll', 'price': 160, 'image': 'images/veggie_roll.jpg'},
            {'name': 'Aloo tikki Wrap', 'price': 160, 'image': 'images/Aloo Tikki Wrap.jpeg'}
        ],
        'Momos': [
            {'name': 'Momos', 'price': 190, 'image': 'images/Momos.jpeg'},
            {'name': 'Tandori Momos', 'price': 280, 'image': 'images/tandori_momos.jpeg'},
            {'name': 'Afghani Momos', 'price': 350, 'image': 'images/afghani_momos.jpeg'},
        ]
    }
    return render(request, 'menu.html', {'menu_data': menu_data})


def book_table_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        booking = Booking(name=name, time=time, guests=guests)
        booking.save()

        message = f"Thank you {name}, your table for {guests} guests at {time} is booked!"
        return render(request, 'book_table.html', {'message': message})
    
    return render(request, 'book_table.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = ContactMessage(name=name, email=email, message=message)
        contact.save()

        success_message = f"Thanks {name}, we will get back to you soon!"
        return render(request, 'contact.html', {'message': success_message})
    
    return render(request, 'contact.html')


def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        image = request.POST.get('image')
        quantity = int(request.POST.get('quantity', 1))

        existing_item = CartItem.objects.filter(name=name).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            CartItem.objects.create(name=name, price=price, image=image, quantity=quantity)

        return redirect('cart')


def update_quantity(request, name):
    item = get_object_or_404(CartItem, name=name)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            item.quantity += 1
        elif action == 'decrease' and item.quantity > 1:
            item.quantity -= 1
        item.save()
    return redirect('cart')


def remove_from_cart(request, name):
    item = get_object_or_404(CartItem, name=name)
    item.delete()
    return redirect('cart')


def checkout_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})


def payment_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        method = request.POST.get('payment_method')
        upi_id = request.POST.get('upi_id')
        user_email = request.POST.get('user_email')

        request.session['payment_method'] = method
        request.session['upi_id'] = upi_id
        request.session['user_email'] = user_email

        # Clear the cart
        CartItem.objects.all().delete()

        if method == "Cash on Delivery":
            return redirect('receipt')
        else:
            return redirect('payment_success')

    return render(request, 'payment.html', {'total': total})


def process_payment(request):
    if request.method == 'POST':
        return redirect('payment_success')
    return redirect('cart')


def payment_success_view(request):
    return render(request, 'payment_success.html')


def receipt_view(request):
    payment_method = request.session.get('payment_method', 'N/A')
    upi_id = request.session.get('upi_id', '')
    user_email = request.session.get('user_email', '')

    current_date = datetime.now().strftime('%B %d, %Y - %I:%M %p')
    order_id = "#RST" + str(random.randint(100000, 999999))

    if user_email:
        send_mail(
            subject='Order Confirmation - MyRestaurant',
            message=f'''
🎉 Thank you for your order!

🧾 Order ID: {order_id}
📅 Date: {current_date}
💳 Payment Method: {payment_method}

We are preparing your food 🍽️

- MyRestaurant
''',
            from_email='shrutibhalerao03@gmail.com',
            recipient_list=[user_email],
            fail_silently=False,
        )

    return render(request, 'receipt.html', {
        'payment_method': payment_method,
        'upi_id': upi_id,
        'current_date': current_date,
        'order_id': order_id
    })

@csrf_exempt
def chatbot_reply(request):
    if request.method != "POST":
        return JsonResponse({"reply": "Invalid request method."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8") if isinstance(request.body, (bytes, bytearray)) else request.body)
        user_message = (data.get("message", "") or "").strip()
        if not user_message:
            return JsonResponse({"reply": "Please type something so I can help!"})

        msg = user_message.lower()

        small_talk = {
            "hi": ["Hi! 👋 How can I help you today?", "Hello! Welcome to MyRestaurant — how can I assist?"],
            "hello": ["Hello! 😊 What would you like to know?", "Hey there — how can I help you?"],
            "how are you": ["I'm just a friendly bot — ready to help you order delicious food! 🍔", "Doing great! How can I help you today?"],
            "who are you": ["I'm MyRestaurant's virtual assistant. I can help with menu, timings, booking and orders.", "I'm the restaurant assistant bot — here to help :)"],
            "thanks": ["You're welcome! 😊", "Glad I could help!"],
            "thank you": ["Anytime! If you want to order, just tell me what you'd like."],
            "okay":["Anything else???"],
            "yes":["Sure, I'm ready to listen..."]
        }

        # try to match small-talk phrases first (exact phrase or containing)
        for key, replies in small_talk.items():
            if key in msg:
                return JsonResponse({"reply": random.choice(replies)})

        faqs = {
            "menu": 'Our menu includes Pizza, Burger, Pasta, Garlic Bread, Fries, Wraps and Momos. <a href="/menu/" target="_blank" style="color: Brown; text-decoration: underline; font-style:italic ;">View Menu</a>',
            "timings": "We are open from 10:00 AM to 11:00 PM every day.",
            "location": "We're located at MG Road, Pune, near City Mall. (Example address — update as needed.)",
            "booking": 'You can book a table from the "Book Table" page <a href="/book/" style="color: Brown; text-decoration: underline,italic ;">View table</a> or call us at +91-9876543210.',
            "payment methods": "We accept Cash, UPI, Credit/Debit cards and online payments via Razorpay.",
            "delivery area": "We deliver within a 5 km radius. If you give your area name, I can check delivery availability.",
            "offers": "Current offers: Buy 1 Pizza, Get 1 Cold Drink Free on Fridays; 20% off on weekends.",
            "price": 'Average meal price ranges from ₹150 to ₹500 depending on items. For exact item prices check the menu page. <a href="/menu/" style="color:Brown; text-decoration: underline,italic;">View menu</a>'
        }

        for key in faqs.keys():
            if key in msg:
                return JsonResponse({"reply": faqs[key]})

        closest = difflib.get_close_matches(msg, faqs.keys(), n=1, cutoff=0.45)
        if closest:
            return JsonResponse({"reply": faqs[closest[0]]})

        if re.search(r"\bwhere\b.*\b(location|located|address)\b", msg) or "where" in msg and "located" in msg:
            return JsonResponse({"reply": faqs["location"]})
        if re.search(r"\b(book|booking|reserve|reservation)\b", msg):
            return JsonResponse({"reply": faqs["booking"]})
        if re.search(r"\b(payment|pay|card|upi)\b", msg):
            return JsonResponse({"reply": faqs["payment methods"]})
        if re.search(r"\b(deliver|delivery|deliveries|deliver to)\b", msg):
            return JsonResponse({"reply": faqs["delivery area"]})
        if re.search(r"\b(menu|what do you serve|what's available)\b", msg):
            return JsonResponse({"reply": faqs["menu"]})
        if re.search(r"\b(offer|discount|deal|sale)\b", msg):
            return JsonResponse({"reply": faqs["offers"]})
        if re.search(r"\b(price|cost|how much|rate)\b", msg):
            return JsonResponse({"reply": faqs["price"]})

        fallback = (
            "Sorry, I didn't understand that. You can ask about our menu, timings, location, booking, "
            "payment methods, offers or delivery area. If you want, type 'menu' or 'timings'."
        )
        return JsonResponse({"reply": fallback})

    except Exception as e:
        # safe error reply
        return JsonResponse({"reply": "Sorry, something went wrong on server. " + str(e)}, status=500)
