from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from django.db.models.signals import post_save, pre_save

from helpers.models import SortableModel

# Create your models here.
class QuizManager(models.Manager):
 	def create_quiz(self, creator, title, password, start_msg='', end_msg=''):
 		quiz = self.model(
 			creator = creator,
 			title = title,
 		)
 		quiz.set_password(password)
 		if start_msg != '':
 			quiz.before_start_message = start_msg
 		if end_msg != '':
 			quiz.after_end_message = end_msg
 		quiz.save()
 		return quiz



class Quiz(models.Model):
	start_msg = "Select an answer for every question. Unanswered questions will be scored as incorrect."
	end_msg = "Close this browser when you are done."
	creator = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	password = models.CharField(max_length=128)
	before_start_message = models.TextField(null=True, blank=True, default=start_msg)
	after_end_message = models.TextField(null=True, blank=True, default=end_msg)
	show_score = models.BooleanField("show taker's score quiz",default=False)
	show_answers = models.BooleanField("show taker's answers and evaluation after quiz",default=False)
	is_active = models.BooleanField('active',default=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = QuizManager()

	class Meta:
		ordering = ['-timestamp']
		verbose_name = "Quiz"
		verbose_name_plural = "Quizzes"

	def __unicode__(self):
		return self.title

	def set_password(self, raw_password):
		self.password = make_password(raw_password)

	def validate_password(self, raw_password):
		return check_password(raw_password, self.password)

	def question_count(self):
		return len(self.question_set.all())

	def taker_count(self):
		return len(self.taker_set.all())



class Question(SortableModel):
	QUESTION_TYPE_CHOICES = (
		('fb', 'Fill in the Blank'),
		('tf', 'True or False'),
		('mc', 'Multiple Choice'),
	)

	quiz = models.ForeignKey(Quiz)
	question_text = models.TextField()
	question_type = models.CharField(max_length=2,
									default='fb',
									choices=QUESTION_TYPE_CHOICES)
	answer_text = models.TextField()

	def __unicode__(self):
		return self.question_text

	def get_choices(self):
		if self.question_type == 'tf':
			return ['True','False']
		if self.question_type == 'mc':
			choices = []
			for choice in self.choice_set.all():
				choices.append(choice.choice_text)
			return choices
		return []



def question_post_save_receiver(sender, instance, *args, **kwargs):
	"""
	Update Quiz.updated on save
	"""
	instance.quiz.save()
    
post_save.connect(question_post_save_receiver, sender=Question)
pre_save.connect(Question.pre_save, sender=Question)



class Choice(SortableModel):
	question = models.ForeignKey(Question)
	choice_text = models.TextField()
	is_correct = models.BooleanField(default=False)

	def __unicode__(self):
		return self.choice_text


def choice_post_save_receiver(sender, instance, *args, **kwargs):
	"""
	Update Quiz.updated on save
	"""
	instance.question.quiz.save()
    
post_save.connect(choice_post_save_receiver, sender=Choice)
pre_save.connect(Choice.pre_save, sender=Choice)



class Taker(models.Model):
	quiz = models.ForeignKey(Quiz)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	score = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s" %(self.get_full_name())

	def get_full_name(self):
		return "%s, %s" %(self.last_name, self.first_name)



class Answer(models.Model):
	taker = models.ForeignKey(Taker)
	question = models.ForeignKey(Question)
	answer = answer = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return "%s answered %s on %s" %(self.taker.get_full_name(), self.answer, self.question.question_text)
    