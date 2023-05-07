from django.db import models

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'text': f'Text {i}',
        'tag': f'tag {i}'    
    } for i in range(20)
]

TAGS = [
    {
        'name': f'tag_{i}'
    } for i in range(10)
]

ANSWERS = [
    {
        'id': i,
        'title': f'Answer {i}',
        'text': f'Text {i}',
        'tag': f'tag {i}'    
    } for i in range(10)
]


class profiles(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(default=0)

class tags(models.Model):
    name = models.CharField(max_length=255)
    
class questions(models.Model):
    author_id = models.ForeignKey(profiles, on_delete=models.CASCADE, verbose_name='Author')
    header = models.CharField(max_length=255)
    text = models.TextField
    likes_count = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(tags)
    
class answers(models.Model):
    question_id = models.ForeignKey(questions, on_delete=models.CASCADE, verbose_name='Question')
    author_id = models.ForeignKey(profiles, on_delete=models.CASCADE, verbose_name='Author')
    header = models.CharField(max_length=255)
    text = models.TextField
    correct = models.BooleanField(default=False)
    likes_count = models.IntegerField(default=0)

class likes(models.Model):
    status = models.IntegerField(default=0)
    question_id = models.ForeignKey(questions, on_delete=models.CASCADE, verbose_name='Question', related_name='question_likes', null=True, blank=True)
    answer_id = models.ForeignKey(questions, on_delete=models.CASCADE, verbose_name='Answer', related_name='answer_likes', null=True, blank=True)
    author_id = models.ForeignKey(profiles, on_delete=models.CASCADE, verbose_name='Author')

