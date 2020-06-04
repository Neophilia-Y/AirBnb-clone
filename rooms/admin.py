from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width=50px src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = [
        PhotoInline,
    ]
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("More about Space", {"fields": ("amenities", "facilities", "house_rules")}),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": ("beds", "guests", "bedrooms", "baths"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "address",
        "instant_book",
        "count_amenity",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)
    ordering = ("price", "name")

    search_fileds = ("city", "host__username")  # None icontain, ^,=
    # 찾고 싶은 변수 다음에 언더바 2개

    filter_horizontal = ("amenities", "facilities", "house_rules")

    # filter에 들어갈 함수 생성 self가 RoomAdmin, obj는 row(인스턴스들)
    def count_amenity(self, obj):
        return obj.amenities.count()

    def count_photos(
        self, obj
    ):  # 우리의 obj는 Room이지만 photo에서 room을 포린키로 잡고 있으므로 photo_set을 갖고 있다
        return obj.photos.count()

    count_amenity.short_description = "Hello Potato"
    count_photos.short_description = "Photo Count"
    count_amenity.short_description = "Amenity Count"
