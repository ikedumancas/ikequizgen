from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	username = forms.CharField(required=True, 
		widget=forms.TextInput(attrs={"required":"required"}),
		help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
		)
	email = forms.EmailField(required=True, 
		widget=forms.EmailInput(attrs={"required":"required"}))
	first_name = forms.CharField(required=True, 
		widget=forms.TextInput(attrs={"required":"required"}))
	last_name = forms.CharField(required=True, 
		widget=forms.TextInput(attrs={"required":"required"}))
	password1 = forms.CharField(label="Password", 
		widget=forms.PasswordInput(attrs={"required":"required"}))
	password2 = forms.CharField(label="Password confirmation", 
		widget=forms.PasswordInput(attrs={"required":"required"}),
		help_text="Enter the same password as above, for verification.")

	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "password1", "password2",)

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user