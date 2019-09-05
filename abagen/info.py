# -*- coding: utf-8 -*-
"""
Defines information about the abagen distribution
"""

long_description = """
abagen: A toolbox for the Allen Brain Atlas genetics data
=========================================================

This package provides a Python interface for fetching and working with the
`Allen Human Brain Atlas`_ (AHBA) microarray expression data.

.. image:: https://travis-ci.org/rmarkello/abagen.svg?branch=master
   :target: https://travis-ci.org/rmarkello/abagen
.. image:: https://codecov.io/gh/rmarkello/abagen/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rmarkello/abagen
.. image:: https://readthedocs.org/projects/abagen/badge/?version=latest
   :target: https://abagen.readthedocs.io/en/stable
.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. _readme_overview:

Overview
--------

In 2013, the Allen Institute for Brain Science released the `Allen Human Brain
Atlas`_, a dataset containing microarray expression data collected from six
human brains [2]_ . This dataset has offered an unprecedented opportunity to
examine the genetic underpinnings of the human brain, and has already yielded
novel insight into e.g., `adolescent brain development <https://www.pnas.org/
content/113/32/9105.long>`__ and `functional brain organization <https://
science.sciencemag.org/content/348/6240/1241.long>`__.

However, in order to be effectively used in most analyses, the AHBA microarray
expression data often needs to be (1) collapsed into regions of interest (e.g.,
parcels or networks), and (2) combined across donors. While this may
potentially seem trivial, there are numerous analytic choices in these steps
that can dramatically influence the resulting data and any downstream analyses.
Arnatkevičiūte et al., 2019 [1]_ provided a thorough treatment of this in a
`recent manuscript <https://www.sciencedirect.com/science/article/pii/
S1053811919300114>`__, demonstrating how the techniques and code used to
prepare the raw AHBA data have varied widely across published reports.

The current Python package, ``abagen``, aims to provide reproducible workflows
for processing and preparing the AHBA microarray expression data for analysis.

.. _readme_requirements:

Installation requirements
-------------------------
Currently, ``abagen`` works with Python 3.5+ and requires a few dependencies:

    - nibabel
    - numpy (>=1.14.0)
    - pandas, and
    - scipy

There are some additional (optional) dependencies you can install to speed up
some functions:

    - fastparquet
    - python-snappy

These latter packages are primarily used to facilitate loading the (rather
large) microarray expression dataframes provided by the Allen Institute.

For detailed information on how to install ``abagen``, including these
dependencies, refer to our `installation instructions`_.

.. _readme_usage:

Getting started
---------------

At it's core, using ``abagen`` is as simple as:

.. code-block:: python

    >>> import abagen
    >>> expression = abagen.get_expression_data('myatlas.nii.gz')

where ``'myatlas.nii.gz'`` points to a Nifti file that defines a brain
parcellation in MNI space.

This function can also be called from the command line with:

.. code-block:: bash

    $ abagen --output-file expression.csv myatlas.nii.gz

For more detailed instructions on how to get started using abagen please refer
to our `documentation`_!

.. _readme_development:

Development and getting involved
--------------------------------

This package has been largely developed in the spare time of a single graduate
student (`@rmarkello <https://github.com/rmarkello>`__) with help from some
incredible `contributors`_. While it would be |sparkles| amazing |sparkles| if
anyone else finds it helpful, given the limited time constraints of graduate
school the current package is not currently accepting requests for new
features.

However, if you're interested in getting involved in the project (and perhaps
adding a feature yourself!) we're thrilled to welcome new contributors. You
should start by reading our `contributing guidelines`_ and `code of conduct`_.
Once you're done with that, take a look at our `GitHub issues`_ to see if
there's anything you might like to work on. Alternatively, if you've found a
bug, are experiencing a problem, or have a question about using the package,
create a new issue with some information about it!

.. _readme_acknowledgments:

Acknowledgments
---------------

While this package was initially created in early 2018, many of the current
functions in the project were inspired by the workflow laid out in
Arnatkevičiūte et al., 2019. As such, if you use this code it would be good
to (1) provide a link back to the ``abagen`` repository with the version of the
code used, and (2) cite their paper:

.. [1] Arnatkevic̆iūtė, A., Fulcher, B. D., & Fornito, A. (2019). A practical
   guide to linking brain-wide gene expression and neuroimaging data.
   NeuroImage, 189, 353-367.

Additionally, please cite the following paper as the source of all microarray
expression data from the Allen Human Brain Atlas:

.. [2] Hawrylycz, M.J. et al. (2012) An anatomically comprehensive atlas of the
   adult human transcriptome. Nature, 489, 391-399. doi:10.1038/nature11405

.. _readme_licensing:

License Information
-------------------

This codebase is licensed under the `3-clause BSD license`_. The full license
can be found in the `LICENSE`_ file in the ``abagen`` distribution.

Reannotated gene information located at ``abagen/data/reannotated.csv.gz`` is
taken from Arnatkevičiūte et al., 2018 and is separately licensed under the `CC
BY 4.0`_; these data can also be found on `figshare <https://figshare.com/s/
441295fe494375aa0c13>`__.

Corrected MNI coordinates used to match AHBA tissues samples to MNI space
located at ``abagen/data/corrected_mni_coordinates.csv`` are taken from the
`alleninf package`_, provided under the `3-clause BSD license`_.

All microarray expression data is copyrighted under `non-commercial reuse
policies`_ by the Allen Institute for Brain Science (© 2010 Allen Institute for
Brain Science. Allen Human Brain Atlas. Available from: `Allen Human Brain
Atlas`_).

All trademarks referenced herein are property of their respective holders.

.. |sparkles| replace:: ✨
.. _3-clause BSD license: https://opensource.org/licenses/BSD-3-Clause
.. _Allen Human Brain Atlas: https://human.brain-map.org/
.. _alleninf package: https://github.com/chrisfilo/alleninf
.. _CC BY 4.0: https://creativecommons.org/licenses/by/4.0/legalcode
.. _code of conduct: https://github.com/rmarkello/abagen/blob/master/CODE_OF_CONDUCT.md
.. _contributing guidelines: https://github.com/rmarkello/abagen/blob/master/CONTRIBUTING.md
.. _contributors: https://github.com/rmarkello/abagen/graphs/contributors
.. _documentation: https://abagen.readthedocs.io
.. _GitHub issues: https://github.com/rmarkello/abagen/issues
.. _installation instructions: https://abagen.readthedocs.io/en/stable/installation.html
.. _LICENSE: https://github.com/rmarkello/abagen/blob/master/LICENSE
.. _non-commercial reuse policies: https://alleninstitute.org/legal/terms-use/
"""  # noqa
