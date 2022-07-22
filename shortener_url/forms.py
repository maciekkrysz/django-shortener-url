from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['alias', 'link_to']

    def clean(self):
        data = self.cleaned_data
        alias = data.get("alias")
        link_to = data.get("link_to")
        
        try:
            val_link = URLValidator()
            val_link(link_to)
        except ValidationError:
            self.add_error("link_to", f"\"{link_to}\" is not correct url. Please try another link.")
                
        if alias is not None:
            qs = Link.objects.filter(alias__icontains=alias)
            if qs.exists():
                self.add_error("alias", f"\"{alias}\" is already in use. Please pick another one.")
        return data