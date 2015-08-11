from django import forms

from .models import Quiz

class QuickQuizCreate(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}),max_length=200)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required':'required'}), min_length=5, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required':'required'}), min_length=5, label="Re-enter Password")

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1:
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError("Passwords don't match")
			return password2
		raise forms.ValidationError("Password error!")


class FullQuizCreateForm(forms.Form):
	start_msg_txt = "Select an answer for every question. Unanswered questions will be scored as incorrect."
	end_msg_txt = "Close this browser when you are done."
	
	title = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}),max_length=200)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required':'required'}), min_length=5, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required':'required'}), min_length=5, label="Re-enter Password")
	start_msg = forms.CharField(widget=forms.Textarea(), label="Beginning Message", required=False, initial=start_msg_txt)
	end_msg = forms.CharField(widget=forms.Textarea(), label="End Message", required=False, initial=end_msg_txt)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1:
			if len(password2) < 5:
				raise forms.ValidationError("Password is too short")
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError("Passwords don't match")
			return password2
		raise forms.ValidationError("Password error!")


class EditQuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ('title', 'before_start_message', 'after_end_message', 'show_score', 'show_answers', 'is_active')