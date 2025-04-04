from .models import Feedback,Product,User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile=forms.CharField(max_length=10)
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2','mobile']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','image','price','category','location','phone']



from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']  # You can customize this if needed
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }


from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount (INR)', max_digits=10, decimal_places=2)






