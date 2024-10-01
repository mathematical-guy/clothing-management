from django.db import models
from common_app.models import BaseModel


class LaundryEvent(BaseModel):
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Laundry - {self.id} - {self.created_on}"


class LaundryCloth(BaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    laundry = models.ForeignKey(to=LaundryEvent, on_delete=models.CASCADE, related_name="laundry_event_clothes")
    description = models.TextField(null=True, blank=True)
    is_ready = models.BooleanField(default=False)
    image = models.ImageField(upload_to="media/laundry_clothes/")
    ready_on = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = "Laundry Clothes"

    def __str__(self):
        return f"{self.name} - {self.laundry.name}"
