import django

def get_Django_version():
    return django.get_version()

print get_Django_version()