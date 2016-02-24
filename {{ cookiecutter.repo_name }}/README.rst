================================
{{ cookiecutter.project_title }}
================================

{{ cookiecutter.project_description }}

Usage
=====

1. Make virtualenv

::

   $ virtualenv --python=python2.7 venv
   $ . venv/bin/activate
   (venv)$

2. install funkload-friendly

::

   (venv)$ easy_install funkload-friendly

3. Copy "local.conf.tmpl" to "local.conf".

::

   $ cp local.conf.tmpl local.conf

4. Run test.

::

   $ fl-run-test --config=local.conf {{ cookiecutter.module_name }}

5. Run benchmark.

::

   $ fl-run-bench --config=local.conf {{ cookiecutter.module_name }} {{ cookiecutter.class_name }}.test_top_page
