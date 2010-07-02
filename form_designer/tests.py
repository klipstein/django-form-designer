from django.conf import settings
from django.db import models
from django.test import TestCase

from forms import DynamicForm
from models import AbstractField

class FieldStub(AbstractField):
    pass

class ModelChoice(models.Model):
    choice = models.CharField(max_length=80)

    def __unicode__(self):
        return u'%s' % self.choice

# Register our test model so django knows about it
# models.register_models('form_designer', ['ModelChoice'])

class DynamicFormTestCase(TestCase):
    """
    Do some sanity checking to make sure that what we are putting into our
    model is what we are gettings out.
    """
    def setUp(self):
        self.form = DynamicForm
        self.old_LANGUAGES = settings.LANGUAGES
        self.old_LANGUAGE_CODE = settings.LANGUAGE_CODE
        settings.LANGUAGES = (('en', 'English'),)
        settings.LANGUAGE_CODE = 'en'

        # Create some formfields so we can test
        choices = ('one', 'two', 'three', 'four', 'five')
        fields = (
            'django.forms.CharField',
            'django.forms.EmailField',
            'django.forms.URLField',
            'django.forms.IntegerField',
            'django.forms.DecimalField',
            'django.forms.BooleanField',
            'django.forms.DateField',
            'django.forms.DateTimeField',
            'django.forms.TimeField',
            'django.forms.ChoiceField',
            'django.forms.MultipleChoiceField',
            'django.forms.ModelChoiceField',
            'django.forms.ModelMultipleChoiceField',
            'django.forms.RegexField'
        )
        for field in fields:
            FieldStub.objects.create(
                name=field.split('.')[-1],
                choice_model='form_designer.tests.ModelChoice',
                choice_values='\n'.join(choices),
                field_class=field,
                regex=r'^[0-9]$'
            )
        for choice in choices:
            ModelChoice.objects.create(choice=choice)

    def tearDown(self):
        settings.LANGUAGES = self.old_LANGUAGES
        settings.LANGUAGE_CODE = self.old_LANGUAGE_CODE

    def test_empty_form(self):
        query_set = FieldStub.objects.filter(name='')
        self.assert_(self.form(query_set, data={}).is_valid())
        self.assertFalse(self.form(query_set).is_valid())

    def test_char_field(self):
        query_set = FieldStub.objects.filter(name='CharField')
        self.assert_(self.form(query_set, data={
            'CharField': 'testage'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'CharField': ''
        }).is_valid())

    def test_email_field(self):
        query_set = FieldStub.objects.filter(name='EmailField')
        self.assert_(self.form(query_set, data={
            'EmailField': 'bob@example.com'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'EmailField': 'testage'
        }).is_valid())

    def test_url_field(self):
        query_set = FieldStub.objects.filter(name='URLField')
        self.assert_(self.form(query_set, data={
            'URLField': 'http://example.com'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'URLField': 'testage'
        }).is_valid())

    def test_integer_field(self):
        query_set = FieldStub.objects.filter(name='IntegerField')
        self.assert_(self.form(query_set, data={
            'IntegerField': '42'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'IntegerField': 'testage'
        }).is_valid())

    def test_decimal_field(self):
        query_set = FieldStub.objects.filter(name='DecimalField')
        self.assert_(self.form(query_set, data={
            'DecimalField': '42.40'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'DecimalField': 'testage'
        }).is_valid())

    def test_bool_field(self):
        query_set = FieldStub.objects.filter(name='BooleanField')
        self.assert_(self.form(query_set, data={
            'BooleanField': '1'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'BooleanField': ''
        }).is_valid())

    def test_date_field(self):
        query_set = FieldStub.objects.filter(name='DateField')
        self.assert_(self.form(query_set, data={
            'DateField': '1985-12-25'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'DateField': 'testage'
        }).is_valid())

    def test_date_time_field(self):
        query_set = FieldStub.objects.filter(name='DateTimeField')
        self.assert_(self.form(query_set, data={
            'DateTimeField': '1985-12-25 08:42:00'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'DateTimeField': 'testage'
        }).is_valid())

    def test_time_field(self):
        query_set = FieldStub.objects.filter(name='TimeField')
        self.assert_(self.form(query_set, data={
            'TimeField': '08:42:00'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'TimeField': 'testage'
        }).is_valid())

    def test_choice_field(self):
        query_set = FieldStub.objects.filter(name='ChoiceField')
        self.assert_(self.form(query_set, data={
            'ChoiceField': 'two'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'ChoiceField': 'testage'
        }).is_valid())

    def test_multiple_choice_field(self):
        query_set = FieldStub.objects.filter(name='MultipleChoiceField')
        self.assert_(self.form(query_set, data={
            'MultipleChoiceField': ['two', 'three']
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'MultipleChoiceField': 'testage'
        }).is_valid())

    # TODO: Get these test working
    def test_model_choice_field(self):
        query_set = FieldStub.objects.filter(name='ModelChoiceField')
        # print ModelChoice.objects.all()
        # print self.form(query_set)
        # self.assert_(self.form(query_set, data={
        #     'ModelChoiceField': 'two'
        # }).is_valid())
        # self.assertFalse(self.form(query_set, data={
        #     'ModelChoiceField': 'testage'
        # }).is_valid())

    # def test_model_multiple_choice_field(self):
    #     query_set = FieldStub.objects.filter(name='ModelMultipleChoiceField')
    #     self.assert_(self.form(query_set, data={
    #         'ModelMultipleChoiceField': 'testage'
    #     }).is_valid())
    #     self.assertFalse(self.form(query_set, data={
    #         'ModelMultipleChoiceField': 'testage'
    #     }).is_valid())

    def test_re_field(self):
        query_set = FieldStub.objects.filter(name='RegexField')
        self.assert_(self.form(query_set, data={
            'RegexField': '2'
        }).is_valid())
        self.assertFalse(self.form(query_set, data={
            'RegexField': '369'
        }).is_valid())

class FormDefinitionTestCase(TestCase):
    pass

class FormDefinitionFieldTestCase(TestCase):
    pass