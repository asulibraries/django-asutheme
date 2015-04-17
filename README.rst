Arizona State University Web Standards Theme for Django
=======================================================

This project provides base templates for use in Django apps that need to
conform to the ASU `University Web Design Standards
<https://hub.asu.edu/brand-hq/web-standards/university-standards>`_.

It relies on the assets created by the `ASU Web Standards Bootstrap project
<https://github.com/gios-asu/ASU-Web-Standards-Bootstrap>`_ provided by
the `Global Institute of Sustainability <https://github.com/gios-asu>`_.

Installation & Usage
--------------------

Install using pip (or easy_install)::

    pip install django-asutheme

Add ``'asutheme'`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'django.contrib.admin',
        'asutheme',
    )

You can now extend the base template and add to/override defined blocks::

    {% extend asutheme/base.html %}

    {% block asu_site_title_main %}
        <a href="https://lib.asu.edu" title="Arizona State University - Libraries">ASU Libraries</a>
    {% endblock %}

    {% block navbar_content %}
        <li><a href="/media">Media</a></li>
    {% endblock %}

    {% block super_footer_brand %}
        <img src="/static/images/libraries_logo_footer.png" alt="ASU Libraries Logo">
        <address>
            ...
        </address>
    {% endblock %}
