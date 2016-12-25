"""
WSGI config for jakobmorrison project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys, site

# add site dir
site.addsitedir('/root/.virtualenvs/jakobmorrison_env/lib/python3.5/site-packages/')

# Calculate the path based on the location of the WSGI script.
sys.path.append('/root/jakobmorrison')
sys.path.append('/root/jakobmorrison/jakobmorrison')

# Add the path to 3rd party django application and to django itself.
#sys.path.append('/root')
os.environ['DJANGO_SETTINGS_MODULE'] = 'jakobmorrison.apache.override'

# activate_env='/root/.virtualenvs/jakobmorrison_env/bin/activate_this.py'
# exec(open(activate_env).read())

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# This bed is on fire with passion and love
# This podcast is live with Jake and Amir
#
# The neighors complain about the noises above
# The fans screem and shout when the smokeshows appear
#
# But she only comes when shes on top
# But they only come a few times a year
#
# Oh you think your so pretty
# Oh your such a coy diva
#
# My therapest says not to see you no more
# My friends ask me why i listen at all
#
# She says your like a dieses without any cure
# They say you are just two jews that had a web series show
# I put them on blast and show them the starbucks stall
# Shes says you might as well hangyour self in a starbucks stall
#
# She says i am so obsessed i am becoming a bore...no no not
# They say i am obsessed
#
# Oh you think your so pretty
# Oh your such a coy diva



