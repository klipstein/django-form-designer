from django.conf import settings
from django.utils.translation import ugettext_lazy as _

FIELD_CLASSES = getattr(settings, 'FORM_DESIGNER_FIELD_CLASSES', (
    ('forms.CharField', _('Text')),
    ('forms.EmailField', _('E-mail address')),
    ('forms.URLField', _('Web address')),
    ('forms.IntegerField', _('Number')),
    ('forms.DecimalField', _('Decimal number')),
    ('forms.BooleanField', _('Yes/No')),
    ('forms.DateField', _('Date')),
    ('forms.DateTimeField', _('Date & time')),
    ('forms.TimeField', _('Time')),
    ('forms.ChoiceField', _('Choice')),
    ('forms.MultipleChoiceField', _('Multiple Choice')),
    ('forms.ModelChoiceField', _('Model Choice')),
    ('forms.ModelMultipleChoiceField', _('Model Multiple Choice')),
    ('forms.RegexField', _('Regex')),
))

WIDGET_CLASSES = getattr(settings, 'FORM_DESIGNER_WIDGET_CLASSES', (
    ('', _('Default')),
    ('widgets.Textarea', _('Text area')),
    ('widgets.PasswordInput', _('Password input')),
    ('widgets.HiddenInput', _('Hidden input')),
))

FORM_TEMPLATES = getattr(settings, 'FORM_DESIGNER_FORM_TEMPLATES', (
    ('', _('Default')),
    ('html/formdefinition/forms/as_p.html', _('as paragraphs')),
    ('html/formdefinition/forms/as_table.html', _('as table')),
))

# Sequence of two-tuples like (('your_app.models.ModelName', 'My Model'), ...) for limiting the models available to ModelChoiceField and ModelMultipleChoiceField.
# If None, any model can be chosen by entering it as a string
CHOICE_MODEL_CHOICES = getattr(settings, 'FORM_DESIGNER_CHOICE_MODEL_CHOICES', None)

DEFAULT_FORM_TEMPLATE = getattr(settings, 'FORM_DESIGNER_DEFAULT_FORM_TEMPLATE', 'html/formdefinition/forms/as_p.html')

# semicolon is Microsoft Excel default
CSV_EXPORT_DELIMITER = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_DELIMITER', ';')

# include log timestamp in export
CSV_EXPORT_INCLUDE_CREATED = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_INCLUDE_CREATED', True)

CSV_EXPORT_INCLUDE_PK = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_INCLUDE_PK', True)

# include field labels/names in first row if exporting logs for one form only
CSV_EXPORT_INCLUDE_HEADER = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_INCLUDE_HEADER', True)

# include form title if exporting logs for more than one form
CSV_EXPORT_INCLUDE_FORM = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_INCLUDE_FORM', True)

CSV_EXPORT_FILENAME = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_FILENAME', 'export.csv')

CSV_EXPORT_ENCODING = getattr(settings, 'FORM_DESIGNER_CSV_EXPORT_ENCODING', 'utf8')

SUBMIT_FLAG_NAME = getattr(settings, 'FORM_DESIGNER_SUBMIT_FLAG_NAME', 'submit__%s')
