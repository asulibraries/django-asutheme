from django.conf import settings


def container_style(request):
    classname = 'container'
    if getattr('ASU_THEME_FLUID', settings, False):
        classname += '-fluid'
    return {'asutheme_container_class':  classname}
