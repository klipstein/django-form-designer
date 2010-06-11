from django import template
from django.db.models.query import QuerySet
from django.template.defaultfilters import yesno
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.filter
def friendly(value):
    """
    Returns a more "human-friendly" representation of value than repr()
    """
    if isinstance(value, QuerySet):
        qs = value
        value = []
        for object in qs:
            value.append(object.__unicode__())
    if isinstance(value, list):
        value = ', '.join(value)
    if isinstance(value, bool):
        value = yesno(value, u'%s,%s' % (_('yes'), _('no')),)
    if not isinstance(value, basestring):
        value = unicode(value)
    return value
