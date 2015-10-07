pytest-vw
===================================

.. image:: https://travis-ci.org/The-Compiler/pytest-vw.svg?branch=master
    :target: https://travis-ci.org/The-Compiler/pytest-vw
    :alt: See Build Status on Travis CI

VW makes failing test cases succeed in continuous integration tools.

Your primary objective is to ship more code to the world. No need to be slowed down by regressions or new bugs that happen during development.

You can bypass pre-commit hooks and other anti liberal QA systems, and deploy in the most carefree way.

* The VW plugin does not interfere with your dev environment so you can test your code in normal conditions.
* It automatically detects CI environments and makes your test suites succeed even with failing assertions or unwanted exceptions \o/

----

Example
-------

Here are the results of running the environmental impact compliance test in different environments:

.. code-block:: python

	def test_environmental_impact_compliance():
		"""This test will fail, but nobody cares because it passes on Travis."""
		emissions = 12000
		legal_limit = 300
		assert emissions < legal_limit

Running in development environment:

.. image:: http://i.imgur.com/bckPXKc.png
    :alt: Failing test in dev environment

Running in CI environment:

.. image:: http://i.imgur.com/BiKZv25.png
    :alt: Failing test in dev environment

Installation
------------

You can install VW Extension via `pip`_ from `PyPI`_

    pip install pytest-vw

Usage
-----

Run your test suite as normal.

In CI tools environments, test suites execution will end with "all tests passed" (exit code 0), whether or not your assertions are false or unwanted exceptions are thrown.

Configuration
-------------

Under the hood (wink wink), the plugin class detects if the py.test process has been invoked in a CI tools environment. (Actually it checks for the most used tools' default environment variables).

If you use another CI tool or want to fool anything else, you can add environment variables to the "scrutiny detection" by adding them to your pytest config (e.g. ``pytest.ini``)::

	[pytest]
	vw_examinators =
		FOO_CI
		GOVERNMENT_TEST_TOOL

Scandal
-------

Any similarities with a current event concerning (but not limited to) a multinational automobile manufacturer are purely coincidental.

CI tools detection
------------------

Currently detects:

* TravisCI
* Bamboo
* CircleCI
* CodeShip
* GitlabCI
* Hudson
* Jenkins
* TeamCity
* Buildkite

Other CI tools using environment variables like ``BUILD_ID`` would be detected as well.

Frequently asked questions
--------------------------

Really?
	Yes.

Seriosly?
	No.

Why?
	Testing `Cookiecutter`_ and `Cookiecutter-pytest-plugin`_.

Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_. Note they will fail unless you're running them with ``CI=1 tox``.

License
-------

Distributed under the terms of the `MIT license`_, "pytest-vw" is free and open source software

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

Credits
-------

This plugin is heavily inspired by (read: a blatant ripoff of) `phpunit-vw`_

It was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.

.. _`phpunit-vw`: https://github.com/hmlb/phpunit-vw
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/The-Compiler/pytest-vw/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
