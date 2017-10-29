from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(
            username=cleaned_data['login'],
            password=cleaned_data['password'],
        )

        if user is None:
            raise forms.ValidationError('Invalid credentials')

        self.user = user
        return cleaned_data