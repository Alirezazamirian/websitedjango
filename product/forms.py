from django import forms
from .models import Product, Inventory, Order

# این فرم برای بررسی این است که موجودی کل محصول از موجودی آن در انبار هم کمتر نشود
class ProductForm(forms.ModelForm):

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['name']
        product = Product.objects.filter(name__exact=product).first()
        inventory = list(Inventory.objects.filter(product=product).values_list('quantity'))
        used_inventory = 0
        for i in inventory:
            used_inventory += i[0]
        if quantity < used_inventory:
            raise forms.ValidationError(f'با توجه به موجودی انبار ها موجودی این کالا نمیتواند کمتر از {used_inventory} باشد')
        return quantity

    class Meta:
        model = Product
        exclude = []

#___________________________________________

# این فرم برای این است که موجودی انبار ها از موجودی کل یک محصول بیشتر نشود
class InventoryForm(forms.ModelForm):

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        store = self.cleaned_data['store']
        total_inventory = Product.objects.get(id=product.id).quantity
        inventory = list(Inventory.objects.filter(product=product).exclude(store=store).values_list('quantity'))
        used_inventory = 0
        for i in inventory:
            used_inventory += i[0]
        if total_inventory < used_inventory + quantity:
            msg = f'ظرفیت ثبت شده توسط شما {(used_inventory + quantity) - total_inventory } عدد بیشتر از ظرفیت کل این محصول است '
            raise forms.ValidationError(msg)
        return quantity

    class Meta:
        model = Inventory
        exclude = []

class OrderForm(forms.Form):
    quantity_need = forms.IntegerField(min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "مقدار مورد نیاز خود را وارد کنید"}))


class OrderSubmitForm(forms.ModelForm):

    def clean_condition(self):
        condition = self.cleaned_data['condition']
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        store = self.cleaned_data['store']
        inventory = Inventory.objects.get(store=store, product=product)
        product = Product.objects.get(id=inventory.product.id)
        if condition=='failed':
            product.quantity += quantity
            inventory.quantity += quantity
        product.save()
        inventory.save()

        return condition

    class Meta:
        model = Order
        exclude = []