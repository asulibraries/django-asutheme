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

Add ``'asutheme.context_processors.container_style'`` to your list of context processors.
By default the containers are fixed, if you would like them to be fluid add to your settings file.
``ASU_THEME_FLUID = True`` to your settings file.

You can now extend the base template and add to/override defined blocks::

    {% extends 'asutheme/base.html' %}

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

Blocks and Layout Order
-----------------------

The base template defines the followig blocks, listed in the order that
the renderer applies them. Most blocks are empty unless otherwise noted.
Child blocks names appear indented under their parent. Be careful when
overriding parent blocks, as this effectively wipes out any customized
content in child blocks.

-  ``html_attrs``: interpolated inside the ``HTML`` opening tag.
-  ``title:`` appears under the ``TITLE`` element.
-  ``extratitle``: appears under the ``TITLE`` element.
-  ``extrastyle``: appears under the ``HTML>HEAD`` element.
-  ``extrahead``: appears under the ``HTML>HEAD`` element.
-  ``body_attrs``: interpolated under the ``BODY`` opening tag
-  ``asu_main_header``: appears under ``HTML>HEAD``, after the standard
   ASU header section

   -  ``asu_login_link``: (non-empty) ASU login/logout link inside the
      subhead navbar.

-  ``site_name``: Section that identifies the name your site/web
   application. Not to be confused with a page title.

   -  ``asu_site_title_main``
   -  ``asu_site_title_extra``

-  ``navbar``: The main navbar section. See Bootstrap v3 docs for more
   info: https://getbootstrap.com/components/#navbar

   -  ``navbar_brand_link_text``: brand text
   -  ``navbar_content``: appears under a navbar UL element. Customize
      by adding LI elements.

-  ``main_content``: The page-specific body of the page. Appears under
   ``DIV#content.site-content`` element.
-  ``footer``: top-level container for the “super footer” (for
   site-specific content) and the “global footer” (ASU standard content
   that appears on the bottom of every page).

   -  ``super_footer``:

      -  ``super_footer_brand_col``: Leftmost column of the super footer
         row. Column width is ``.col-md-4.col-sm-12``.

         -  ``super_footer_brand``: brand text to appear in the
            left-most column of the site-specific footer.

      -  ``super_footer_content``: blank block that appears ender the
         super-footer after the brand column. *Note:* since this block
         appears in a ``.row`` you will want to put any custom content
         in a bootstrap “column”, e.g.
         ``<div class=".col-md-8">my footer content</div>``

-  ``global_footer``: (non-empty): the ASU Standard footer. You probably
   don’t want to override this.
-  ``extrajs``: section for adding ``SCRIPT`` includes.
-  ``google_analytics``: (non-empty) google analytics init script.
   Override with empty block to remove analytics gathering.

   -  ``google_analytics_tracking_id``: override w/ your google
      analytics API key