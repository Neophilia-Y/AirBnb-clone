from django import forms
from . import models
from django_countries.fields import CountryField


class SearchForm(forms.Form):
    # form도 field를 갖는다. Form field Api를 확인하자
    # 장고의 많은 패키지들은 form field를 갖고 있다
    # widegt 옵션을 변경하여 화면에 나오는 방식을 커스트 마이징 할 수 있다.

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
