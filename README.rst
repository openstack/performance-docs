========================
Team and repository tags
========================

.. image:: http://governance.openstack.org/badges/performance-docs.svg
    :target: http://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

OpenStack Performance Documentation
===================================

This repository is for OpenStack performance testing plans, results and investigation documents. 
All documents are in RST format and located in `doc/source/` sub-folder.

Building
========

Prerequisites
-------------

To get started, you need to install all necessary tools:
 * `virtualenv`
 * `pip` (use the latest from `https://bootstrap.pypa.io/get-pip.py`)
 * `tox`
 * system dependencies: `libjpeg-dev`

Run the build
-------------

 $ tox

