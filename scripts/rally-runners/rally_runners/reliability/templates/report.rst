Scenario "{{ report.scenario_name }}"
=========={{ '=' * report.scenario_name | length }}=

This report is generated on results collected by execution of the following
Rally scenario:

.. code-block:: yaml

{{ report.scenario }}

Summary
-------

{% if report.has_errors or report.has_degradation %}

{{ report.summary_table }}

Metrics:
    * `Service downtime` is the time interval between the first and
      the last errors.
    * `MTTR` is the mean time to recover service performance after
      the fault.
    * `Absolute performance degradation` is an absolute difference between
      the mean of operation duration during recovery period and the baseline's.
    * `Relative performance degradation` is the ratio between the mean
      of operation duration during recovery period and the baseline's.

{% else %}

No errors nor performance degradation observed.

{% endif %}

Details
-------

This section contains individual data for particular scenario runs.

{% for item in report.runs %}

Run #{{ loop.index }}
^^^^^^

.. image:: plot_{{ loop.index }}.svg

Baseline
~~~~~~~~

Baseline samples are collected before the start of fault injection. They are
used to estimate service performance degradation after the fault.

{{ item.etalon_table }}

{% if item.errors_table %}
Service downtime
~~~~~~~~~~~~~~~~

The tested service is not available during the following time period(s).

{{ item.errors_table }}
{% endif %}

{% if item.degradation_table %}
Service performance degradation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tested service has measurable performance degradation during the
following time period(s).

{{ item.degradation_table }}
{% endif %}

{% endfor %}
