from django import forms

from form_designer.utils import get_class

class DynamicForm(forms.Form):
    def __init__(self, form_set, initial_data=None, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        for def_field in form_set:
            self.add_defined_field(def_field, initial_data)

    def add_defined_field(self, def_field, initial_data=None):
        if initial_data and initial_data.has_key(def_field.name):
            if not def_field.field_class in ('forms.MultipleChoiceField', 'forms.ModelMultipleChoiceField'):
                def_field.initial = initial_data.get(def_field.name)
            else:
                def_field.initial = initial_data.getlist(def_field.name)
        self.fields[def_field.name] = get_class(def_field.field_class)(**def_field.get_form_field_init_args())