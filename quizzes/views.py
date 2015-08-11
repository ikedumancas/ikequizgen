from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditQuizForm, FullQuizCreateForm, QuickQuizCreate
from .models import Quiz

# Create your views here.
@login_required
def dashboard(request):
	quizzes = request.user.quiz_set.all()
	form = QuickQuizCreate(request.POST or None)
	if form.is_valid():
		pass
	else:
		for error in form.errors:
			form[error].css_classes('validate invalid')
			print error
	context = {
		'quickcreateform':form,
		'quizzes':quizzes
	}
	template = "dashboard.html"
	return render(request, template, context)


@login_required
def quiz_dashboard(request,id):
	quiz = get_object_or_404(Quiz,id=id,creator=request.user)
	form = EditQuizForm(instance=quiz)
	if request.method == "POST":
		form = EditQuizForm(request.POST, instance=quiz)
		if form.is_valid():
			quiz.title = form.cleaned_data['title']
			quiz.before_start_message = form.cleaned_data['before_start_message']
			quiz.after_end_message = form.cleaned_data['after_end_message']
			quiz.show_score = form.cleaned_data['show_score']
			quiz.show_answers = form.cleaned_data['show_answers']
			quiz.is_active = form.cleaned_data['is_active']
			quiz.save()
	context = {
		'form':form,
		'quiz':quiz
	}
	template = "quizzes/quiz_dashboard.html"
	return render(request, template, context)


@login_required
def create_quiz(request):
	form = FullQuizCreateForm(request.POST or None)
	if form.is_valid():
		import urlparse
		prev_path = urlparse.urlparse(request.META.get('HTTP_REFERER')).path
		if reverse('quizzes:dashboard') == prev_path :
			title = form.cleaned_data['title']
			password = form.cleaned_data['password1']
			new_quiz = Quiz.objects.create_quiz(request.user, title=title, password=password)
		else:
			title = form.cleaned_data['title']
			password = form.cleaned_data['password1']
			start_msg = form.cleaned_data['start_msg']
			end_msg = form.cleaned_data['end_msg']
			new_quiz = Quiz.objects.create_quiz(request.user, title=title, password=password, start_msg=start_msg, end_msg=end_msg)
		return redirect('quizzes:quiz_dashboard', id=new_quiz.id)
	context = {
		'form':form
	}
	template = "quizzes/create_quiz.html"
	return render(request, template, context)


@login_required
def quiz_delete(request, id):
	quiz = get_object_or_404(Quiz, id=id)
	quiz.delete()
	return redirect('quizzes:dashboard')