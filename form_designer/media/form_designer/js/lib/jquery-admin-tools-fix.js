// map django's admin jquery to $ and jQuery
// we need to map it that early otherwise jquery-ui would fail to load
// fixes a bug when form-designer is used in conjunction with django-admin-tools
window['jQuery'] = window['$'] = django.jQuery;