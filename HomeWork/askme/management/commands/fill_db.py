from django.core.management.base import BaseCommand
from askme.models import *
from faker import Faker
import random

class Command(BaseCommand):
    
    help = 'filling db'
    fake = Faker()
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of records to add to the database')
                
    def handle(self, **options):
        count = options['count']
        # self.create_users(count)
        # print('Users')
        # self.create_questions(count)
        # print('Questions')
        # self.create_answers(count)
        # print('Answers')
        self.create_tags(count)
        print('Tags')
        self.create_likes(count)
        print('Likes')
        self.create_questions_tags(count)
        print('End')
        
    def create_users(self, count):
        usernames = []
        while len(usernames) <= count:
            new_usernames = [self.fake.user_name() for _ in range(count)]
            usernames += new_usernames
            usernames = list(set(usernames))
                
        users = [User(password=self.fake.password(), username=usernames[i], email=self.fake.email()) for i in range(count)]
        
        profile = [profiles(user=users[i]) for i in range(len(users))]
        User.objects.bulk_create(users)
        profiles.objects.bulk_create(profile)
        
    def create_questions(self, count):
        count = count * 10
        authors = profiles.objects.all()
        print('authors:')
        print(len(authors))
        question = [questions(author=authors[self.fake.random_int(min=1, max=10000)], header=self.fake.sentence(), text=self.fake.text()) for _ in range(count)]
        # , likes_count=self.fake.random_int(min=-10000, max=10000), answers_count=self.fake.random_int(min=0, max=1000)
        questions.objects.bulk_create(question)
        
    def create_answers(self, count):
        # authors_ = profiles.objects.all()
        questions_ = questions.objects.all()
        print('questions:')
        print(len(questions_))
        question_dict = {}
        for question in questions_:
            question_dict[question.pk] = question
            
        count = count * 100
        #  likes_count=self.fake.random_int(min=-10000, max=10000),
        # answer = [answers(header=self.fake.sentence(), text=self.fake.text(), question=questions_[self.fake.random_int(min=1, max=10000)], author=authors_[self.fake.random_int(min=1, max=10000)], correct=self.fake.pybool()) for _ in range(count)]
        print('generating ended')
        # answers.objects.bulk_create(answer)
        print('select ended')
        answer = answers.objects.all()
        for answ in answer:
            question_dict[answ.question.pk].answers_count += 1
            question_dict[answ.question.pk].save()        
        
                    
            
        
    def create_tags(self, count):
        count *= 2
        tag = [tags(name=str(self.fake.words(1))) for _ in range(count)]
        tags.objects.bulk_create(tag)
        
    def create_likes(self, count):
        authors_ = profiles.objects.all()
        questions_ = questions.objects.all()
        answers_ = answers.objects.all()
        count = count * 200
        question_dict = {}
        for question in questions_:
            question_dict[question.pk] = question
        
        print('question dict')
        answer_dict = {}
        for answer in answers_:
            answer_dict[answer.pk] = answer
            
        print('answer dict')
        for i in range(len(questions_)):
            questions_[i].likes_count = 0
        print('question dict is empty')
        
        for i in range(len(answers_)):
            answers_[i].likes_count = 0
        print('answer dict is empty')
        
        
        for i in range(1000):
            if i % 2 == 0:
                like = [likes(status=random.randint(-1, 1), question=questions_[random.randint(1, 10000)], author=authors_[random.randint(1, 10000)]) for _ in range(count//1000)]
            else:
                like = [likes(status=random.randint(-1, 1), author=authors_[random.randint(1, 10000)], answer=answers_[random.randint(1, 1000000)]) for _ in range(count//1000)]
                
            likes.objects.bulk_create(like)
            print(f'done {i}')

        
            for lik in like:    
                if lik.question:
                    question = question_dict[lik.question.pk]
                    question.likes_count += lik.status
                    question.save()
                else:
                    answer = answer_dict[lik.answer.pk]
                    answer.likes_count += lik.status
                    answer.save()
        


    def create_questions_tags(self, count): 
        questions_ = questions.objects.all()
        tags_ = tags.objects.all()
        for question in questions_:
            for i in range(random.randint(0, 5)):
                question.tags.add(tags_[random.randint(1, 2 * count - 1)])
            question.save()
        