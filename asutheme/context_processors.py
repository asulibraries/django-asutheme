from django.conf import settings


def container_style(request):
    classname = 'container'
    if getattr(settings, 'ASU_THEME_FLUID', False):
        classname += '-fluid'
    return {'asutheme_container_class':  classname}
