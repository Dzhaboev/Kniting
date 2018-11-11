from django.forms import ModelForm, Textarea

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgents = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }