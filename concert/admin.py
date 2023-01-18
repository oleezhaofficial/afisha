from django.contrib import admin
from django.utils.html import format_html
from .models import Concert, Artist
from django.utils.http import urlencode
from django.urls import reverse


# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "view_concerts")
    list_filter = ("name", )
    readonly_fields = ("id",)

    def view_concerts(self, obj):

        count = obj.concert_set.count()
        url = (
                reverse("admin:concert_concert_changelist")
                + "?"
                + urlencode({"artist__id": f"{obj.id}"})
        )

        if count % 10 == 1 and count % 100 != 11:
            return format_html('<a href="{}">{} концерт</a>', url, count)
        elif 1 < count % 10 < 5 and (count % 100 > 20 or count % 100 < 10):
            return format_html('<a href="{}">{} концерта</a>', url, count)
        else:
            return format_html('<a href="{}">{} концертов</a>', url, count)



    view_concerts.short_description = "Концерты"


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ("artist_id", "date", "price", "address")
    list_filter = ("artist_id", "age_rating")
    readonly_fields = ("id",)
