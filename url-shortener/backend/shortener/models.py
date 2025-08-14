from django.db import models
from django.core.validators import URLValidator
import string, random


def generate_short_code(length=6):
    """
    Generates a random short code of given length.
    Includes letters and digits.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


class ShortURL(models.Model):
    """
    Stores original URL, short code, and click stats.
    """
    original_url = models.URLField(validators=[URLValidator()])
    short_code = models.CharField(max_length=6, unique=True, editable=False)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.short_code:
            code = generate_short_code()
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            self.short_code = code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
