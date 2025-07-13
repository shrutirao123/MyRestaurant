from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)

    def __str__(self):
        return self.name



class Booking(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.time} ({self.guests} guests)"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject


class CartItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x {self.quantity}"

