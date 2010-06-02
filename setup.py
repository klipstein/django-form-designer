# encoding=utf8
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name = "django-form-designer",
    version = "0.1a1",
    url = 'http://github.com/philomat/django-form-designer',
    license = 'BSD',
    description = "Design contact forms, search forms etc from the Django admin, without writing any code. Integrates with Django CMS.",
    long_description = README,

    author = u'Samuel Lüscher',
    author_email = 'philomat@popkultur.net',
    packages = [
        'form_designer',
        'form_designer.admin',
        'form_designer.templatetags',
    ],
    package_data = {
        'form_designer': [
                'media/form_designer/js/lib/*/js/*.js',
                'media/form_designer/js/lib/*/*.js',
                'templates/admin/form_designer/formlog/change_list.html',
                'templates/*/*/*.html',
                'templates/*/*.html',
                'templates/*/*.txt',
                'locale/*/LC_MESSAGES/*',
            ],
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
