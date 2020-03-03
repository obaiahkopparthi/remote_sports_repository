from django import forms
from multiselectfield import MultiSelectFormField
#from sportsapp .forms import LoginForm,RegistrationForm,MrecordForm,ReportForm


class LoginForm(forms.Form):
    username=forms.CharField(
        label="enter username ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter user name'
            }
        )
    )
    password1=forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )
    )
class RegistrationForm(forms.Form):
    #TYPEOF_REGISTER = (
     #   ('coa', 'coach'),
      #  ('ump', 'umpire'),
       # ('pla', 'player'),
    #)
    #typeof_register = MultiSelectFormField(max_length=200, typeof_register=TYPEOF_REGISTER)
    first_name = forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    last_name = forms.CharField(
        label="enter your last name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your last name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="enter your mobile",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile'
            }
        )
    )
    email = forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    username = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your user name'
            }
        )
    )
    password1 = forms.CharField(
        label="enter password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )
    password2 = forms.CharField(
        label="re-enter password ",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 're-enter password'
            }
        )
    )
    age = forms.IntegerField(
        label="enter your age",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'age'
            }
        )
    )
class MrecordForm(forms.Form):
    match_name = forms.CharField(
        label="enter your match name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your match name'
            }
        )
    )
    match_status = forms.CharField(
        label="match status",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'match result'
            }
        )
    )
    match_coach = forms.CharField(
        label="enter coach name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'coach name'
            }
        )
    )
    match_umpire = forms.CharField(
        label="enter umpire name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'umpire name'
            }
        )
    )
    match_number = forms.IntegerField(
        label="enter match number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'match number'
            }
        )
    )
class ReportForm(forms.Form):
    report_name = forms.CharField(
        label="enter your report name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':' match report name'
            }
        )
    )
    report_status = forms.CharField(
        label="match report status",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'match report'
            }
        )
    )
    report_coach = forms.CharField(
        label="enter coach report",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'coach report'
            }
        )
    )
    report_umpire = forms.CharField(
        label="enter umpire report",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'umpire match report'
            }
        )
    )


