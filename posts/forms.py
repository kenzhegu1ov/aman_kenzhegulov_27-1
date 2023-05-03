from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=4, max_length=254)
    description = forms.Textarea()
    cpu = forms.CharField(min_length=5, max_length=250)
    gpu = forms.CharField(min_length=5, max_length=250)
    price = forms.FloatField()
    rate = forms.FloatField()



class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=5, max_length=350)

