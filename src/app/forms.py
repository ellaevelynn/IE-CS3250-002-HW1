'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student: Isabella Eaton
Description: Homework 01 - Forms for the Recipes Web App
'''

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

# TODO #2: complete the recipe form with the missing fields (title, type, and tags)
class RecipeForm(FlaskForm):
    number = StringField('Recipe#', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    type = SelectField(
        'Type',
        choices=[('breakfast','breakfast'),
                ('appetizer','appetizer'),
                ('side dish','side dish'),
                ('main course','main course'),
                ('dessert','dessert')
                 ],
                 validators=[DataRequired()]
    )
    tags = StringField('Tags', validators=[DataRequired()])
    submit = SubmitField('Submit')