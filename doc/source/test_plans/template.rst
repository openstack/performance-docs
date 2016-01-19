==========================================
Example Test Plan - The title of your plan
==========================================

:status: test plan status - either **draft** or **ready**
:version: test plan version

:Abstract:

  Small description of what will be covered later in the test plan

If needed, please define list of terms that will be used later in the test
plan:

:Conventions:

  - **Some specific term #1:** its explanation

  - **Some specific term #2:** its explanation

  - ...

  - **Some specific term #n:** its explanation

Test Plan
=========

Define the test plan. Test plan can contain several test cases description
using sections, similar to the written below.

Test Environment
----------------

Preparation
^^^^^^^^^^^

Please specify here what needs to be done with the environment to run
this test plan. This can include specific tools installation,
specific OpenStack deployment, etc.

Environment description
^^^^^^^^^^^^^^^^^^^^^^^

Please define here used environment. You can use the scheme below for this
purpose or modify it due to your needs:

* Hardware used (servers, switches, storage, etc.)
* Network scheme
* Software (operating systems, kernel parameters, network interfaces
  configuration, disk partitioning configuration). If distributed provisioning
  systems are to be tested then the parts that are distributed need to be
  described here

Test Case 1: Something very interesting #1
------------------------------------------

Description
^^^^^^^^^^^

Define test case #1. Every test case can contain at least the sections, defined
below.

Parameters
^^^^^^^^^^

Optional section. Can be used if there are multiple test cases differing in
some input parameters - if so, these parameters need to be listed here.

List of performance metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mandatory section. Defines what measurements are in fact done during the test.
To be a good citizen in case of multiple metrics collection, it will be nice to
list the metrics ordered starting with the most important one.

===========================  ===============  =================  =============
Priority                     Value            Measurement Units  Description
===========================  ===============  =================  =============
1 - most important           What's measured  <units>            <description>
2 - less important           What's measured  <units>            <description>
3 - not that much important  What's measured  <units>            <description>
===========================  ===============  =================  =============

Some additional section
^^^^^^^^^^^^^^^^^^^^^^^

Depending on the test case nature, something else may need to be defined.
If so, additional sections with free form titles should be added.

Test Case n: Something very interesting #n
------------------------------------------

Define test case #n using the approach above.

Some additional section
-----------------------

If there are common details for all test cases, that need to be covered
separately, they can be encapsulated in additional free form sections.

Upper level additional section
==============================

If there are additional notes, small pieces of code and configurations, etc.,
they can be defined in additional paragraphs. Huge pieces and large chunks of
configs should be stored in separated files.
