from django import forms
from order.models import Order


#Order 폼 생성
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['realname', 'email', 'address']

        email = forms.CharField(max_length=100)
