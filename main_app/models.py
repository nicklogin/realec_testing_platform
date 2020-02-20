from django.db import models
from django.conf import settings

from random import shuffle

# requires package django-annoying to be installed:
# https://github.com/skorokithakis/django-annoying#readme
# from annoying.fields import AutoOneToOneField

# Create your models here.


class User(models.Model):
    login = models.CharField(max_length=40, primary_key=True)
    full_name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)
    rights = models.CharField(max_length=1,
    choices = (('A','Admin'),('S','Student'),('T','Teacher')))

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     ## не удалять эту строчку, см. обсуждение:
    #     ## https://github.com/skorokithakis/django-annoying/issues/51
    #     User.student = User.student


class Student(models.Model):
    login = models.OneToOneField(User, primary_key=True,
    on_delete=models.CASCADE)
    group = models.CharField(max_length=20, null=True)


class Quizz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL,
    null=True)
    name = models.CharField(max_length=30, null=True, unique=True)
    deadline = models.DateTimeField(null=True)
    strip_answers = models.BooleanField(null=True)


class Folder(models.Model):
    name = models.CharField(max_length=40, unique=True)


class IELTS_Test(models.Model):
    name = models.CharField(max_length=40, unique=True)
    full_grade = models.FloatField(null=True)

class Section(models.Model):
    ielts_test = models.ManyToManyField(IELTS_Test, blank=True)
    text = models.CharField(max_length=100000)
    section_type = models.CharField(max_length=1,
    choices = (('L', 'Listening'), ('R', "Reading"), ("W", "Writing")), null=True)
    supplement = models.FileField(null=True)
    # upload_to=settings.MEDIA_ROOT
    name = models.CharField(max_length=100, null=True)
    # supplement_type = models.CharField(max_length=1,
    # choices=(('p','pdf'), ('i','image'), ('a','audio')), null=True)


class Question(models.Model):
    quiz = models.ManyToManyField(Quizz, blank=True)
    question_text = models.CharField(max_length=1000)
    question_type = models.CharField(max_length=20)
    # question_image = models.ImageField(upload_to='supplies/')
    question_level = models.SmallIntegerField()
    error_tag = models.CharField(max_length=45, null=True)
    folder = models.ManyToManyField(Folder, blank=True)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    case_insensitive = models.BooleanField(default=False)
    # folder_addr = models.CharField(max_length=45, null=True)
    # essay_addr = models.CharField(max_length=45, null=True)
    # question_group = models.CharField(max_length=45, null=True)


    ## special field for retrieving previously created questions:
    ukey = models.CharField(max_length=100, null=True)

    def get_answers(self):
        # print("called")
        wronganswers = self.wronganswer_set.all()
        if wronganswers:
            right_answers = list(self.answer_set.all())
            wrong_answers = list(wronganswers)
            answers = right_answers + wrong_answers
            shuffle(answers)
            return answers
        else:
            return None
        # return ["method called"]

class Answer(models.Model):
    question_id = models.ForeignKey(Question,
    on_delete=models.SET_NULL, null=True)
    answer_text = models.CharField(max_length=300)


class WrongAnswer(models.Model):
    question = models.ForeignKey(Question,
    on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=300)


class Results(models.Model):
    student = models.ForeignKey(User,
    on_delete=models.CASCADE)
    quizz = models.ForeignKey(Quizz, null=True,
    on_delete=models.CASCADE)
    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    mark = models.FloatField()
