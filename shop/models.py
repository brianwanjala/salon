from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - KES {self.price}"

class Barber(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='barbers/')
    specialty = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def clean(self):
        if Booking.objects.filter(
            barber=self.barber,
            date=self.date,
            time=self.time
        ).exists():
            raise ValidationError("This time slot is already booked for this barber.")

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date}"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    barber = models.ForeignKey('Barber', on_delete=models.CASCADE)
    
    date = models.DateField()
    time = models.TimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"