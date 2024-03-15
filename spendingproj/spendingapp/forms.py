from django.forms import ModelForm
from .models import Expense
from .models import Income

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['amount','data','description','category','vendor']

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'data', 'description']