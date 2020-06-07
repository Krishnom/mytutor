from django import forms
from django.contrib.auth import  (authenticate, get_user_model)
from .models import Video


User = get_user_model()

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'title',
            'author',
            'video_file'
        ]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("User not found")

            if not user.check_password(password):
                raise forms.ValidationError("User password is not correct")

            if not user.is_active:
                raise forms.ValidationError("User is inactive")

            return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Enter Email address")
    email2 = forms.EmailField(label="Confirm Email address")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self,*args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Email must match")
        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError("This email id already registered")

        return super(UserRegisterForm, self).clean(*args, **kwargs)