from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'card_name']

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(
            attrs={'placeholder': 'What are you selling'}
        )
        self.fields['description'].widget = forms.Textarea(
            attrs={
                'placeholder': (
                    'Describe the item for sale, condition, '
                    'willing to trade and so on'
                ),
                'class': 'custom-textarea'
            }
        )
        self.fields['price'].widget = forms.NumberInput(
            attrs={'placeholder': 'Price in SEK?', 'class': 'custom-textarea'}
        )
        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.all()
        )
        self.fields['category'].widget.attrs.update({'class': 'custom-select'})
        self.fields['card_name'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Search for Magic Card...',
                'class': 'custom-textarea'
            }
        )