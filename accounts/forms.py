from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order #wich object will generate
        fields = '__all__' #all fields
