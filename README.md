# rest_api_application
django_rest_framework

pip install djangorestframework

pip install django-cors-headers

to view the functionality, disable authentication in settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DATE_FORMAT': '%d.%m.%Y',
}
