=======
PyBayes
=======


.. image:: https://img.shields.io/pypi/v/pybayes.svg
        :target: https://pypi.python.org/pypi/pybayes

.. image:: https://img.shields.io/travis/kashbari/pybayes.svg
        :target: https://travis-ci.com/kashbari/pybayes

.. image:: https://readthedocs.org/projects/pybayes/badge/?version=latest
        :target: https://pybayes.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Bayesian Filters and other Bayesian Estimation Tools.
Resources on Bayesian Filtering/Tracking:

Bayesian Multiple Target Tracking by Stone, Streit, and Corwin
Bayesian Estimation and Tracking by Haug
Applied Optimal Estimation by Gelb


* Free software: MIT license
* Documentation: https://pybayes.readthedocs.io.


Features
--------

* filter.KalmanFilter                 --> KF and EKF implementation
* filter.UnscentedKalmanFilter        --> UKF and SQ-UKF implementation
* filter.ParticleFilter               --> PF implementation
* filter.SquareRootInformationFilter  --> SR-IF implementation

Demo of some of the features:

``
import pybayes
``



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
