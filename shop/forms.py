from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms

class UpdatePasswordForm(SetPasswordForm):
      new_password1=forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder':'رمز بالای 8 کاراکتر'
                                          }
                                    )

    )


      new_password2=forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder':' تکرار رمز  '})
      )

      class Meta:
        model = User
        fields = ('new_password1','new_password2')

class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام '}),
        )

    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام خانوادگی '}),
        )


    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ایمیل  '}),
        )
    

    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام کاربری '}),
        )

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام '}),
        )

    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام خانوادگی '}),
        )


    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ایمیل  '}),
        )
    

    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'نام کاربری '}),
        )

    

    password1=forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder':'رمز'}),

    )


    password2=forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder':' تکرار رمز  '}),

    )
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')




