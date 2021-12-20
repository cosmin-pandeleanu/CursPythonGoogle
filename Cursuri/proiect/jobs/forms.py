from django import forms
from jobs.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'url', 'description', 'customer']

    def __init__(self, pk, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        customer_value = str(cleaned_data.get('customer')).split()[1]
        if self.pk:
            if Job.objects.filter(name__icontains=name_value, active=1).exclude(id=self.pk).exists()\
                    and Job.objects.filter(customer__name=name_value).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Numele deja exista!'])
                # self._errors['customer'] = self.error_class(['Customer-ul deja exista!'])
        else:
            if Job.objects.filter(name__icontains=name_value, active=1).exists()\
                    and Job.objects.filter(customer__name=customer_value).exists():
                self._errors['name'] = self.error_class(['Numele deja exista!!'])
                # self._errors['customer'] = self.error_class(['Customer-ul deja exista!!'])
        return cleaned_data
