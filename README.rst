============
Installation
============

::

  # create & actiavte virtualenv
  pip install -r requirements.txt
  mv simple_rest/local_settings.py.default simple_rest/local_settings.py
  ./manage.py syncdb
  ./manage.py loaddata dummy_data
  ./manage.py runserver