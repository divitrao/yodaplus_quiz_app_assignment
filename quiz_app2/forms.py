from django import forms
from django.db.models import fields
from django.forms import widgets
from django import forms
from django.forms.fields import IntegerField
from .models import model_tests

q_category =(
    ('any','Any Category'),
    ('9','General Knowledge'),
    ('10','Entertainment: Books'),
    ('11','Entertainment: Film'),
    ('12','Entertainment: Music'),
    ('13','Entertainment: Musicals &amp;'),
    ('14','Entertainment: Television'),
    ('15','Entertainment: Video Games'),
    ('16','Entertainment: Board Games'),
    ('17','Science &amp;'),
    ('18','Science: Computers'),
    ('19','Science: Mathematics'),
    ('20','Mythology'),
    ('21','Sports'),
    ('22','Geography'),
    ('23','History'),
    ('24','Politics'),
    ('25','Art'),
    ('26','Celebrities'),
    ('27','Animals'),
    ('28','Vehicles'),
    ('29','Entertainment: Comics'),
    ('30','Science: Gadgets'),
    ('31','Entertainment: Japanese Anime &amp; Manga'),
    ('32','Entertainment: Cartoon &amp; Animations'),
)

q_difficulty =(
    ('any','Any Difficulty'),
    ('easy','EASY'),
    ('medium','MEDIUM'),
    ('hard','HARD')
)

q_Type =(
    ('any','Any Type'),
    ('multiple','Multiple Choice'),
    ('boolean','True / False')
    
)


class Addform(forms.ModelForm):
    class Meta:
        model = model_tests
        fields = ('fav_sub','user_id')

        widgets = {
            'fav_sub':forms.TextInput(),
            'user_id':forms.TextInput(attrs={'id': 'users'}),
            
        }

class Myyform(forms.Form):
    I_Accept_Rules_and_Regulation = forms.BooleanField(required=True)

class user_choice(forms.Form):
    Number_of_question = forms.IntegerField(max_value=49,min_value=10)
    category = forms.ChoiceField(choices=q_category,label='Select Category')
    difficulty = forms.ChoiceField(choices=q_difficulty,label='Select Difficulty')
    Q_type = forms.ChoiceField(choices=q_Type,label='Select Type')

        