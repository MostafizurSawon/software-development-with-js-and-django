from django import forms  # django form api
from django.core import validators

# widget = field to html output
class ContactForm(forms.Form):  # inherit
  name = forms.CharField(label="User Name", help_text="Example: JOHN", required=False, disabled=False, widget = forms.Textarea(attrs={'id':'name_area', 'class': 'name_class1 name_class2', "placeholder":"Enter Your Name"}))
  # name = forms.CharField(label="User Name", initial="Sawon")
  # email = forms.EmailField(label="User Email")
  # age = forms.IntegerField()
  age = forms.CharField(widget=forms.NumberInput())
  # weight = forms.FloatField()
  # balance = forms.DecimalField()
  # check = forms.BooleanField()
  # birthday = forms.DateField(widget=forms.DateInput(attrs = {'type': 'date'}))
  birthday = forms.CharField(widget=forms.DateInput(attrs = {'type': 'date'}))
  appointment = forms.DateTimeField(widget=forms.DateInput(attrs = {'type': 'datetime-local'}))
  CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
  size=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  MEAL = [('P','Pepperoni'), ('M', 'Mashroom'), ('B','Beef')]
  pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
  file = forms.FileField()

class StudentData2(forms.Form):
  name = forms.CharField(widget=forms.TextInput)
  email = forms.CharField(widget=forms.EmailInput)

  def clean(self):
    cleaned_data = super().clean()
    valname = self.cleaned_data['name']
    email = self.cleaned_data['email']
    if len(valname) < 8 :
      raise forms.ValidationError("Need At least 8 characters")
    if '.com' not in email :
      raise forms.ValidationError("Invalid Email")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
   

class StudentData(forms.Form):
    name =forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email =forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),validators.MinValueValidator(24, message="age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = 'File Extension must be ended with .pdf/.png')])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")