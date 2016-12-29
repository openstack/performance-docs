#!/bin/bash
#
WORKDIR="$(cd "$(dirname ${0})" && pwd)"
SCRIPT="${WORKDIR}/$(basename ${0})"
MYSQLUSER="nova"
MYSQPASSWD="password"
MYSQLHOST="mariadb.ccp"
avgdata=$(mysql -u${MYSQLUSER} -p${MYSQPASSWD} -h ${MYSQLHOST} -D nova --skip-column-names --batch -e "select diff from (select avg(unix_timestamp(launched_at) - unix_timestamp(created_at)) as diff from instances where vm_state != 'error' and launched_at >= subtime(now(),'30')) t1 where diff IS NOT NULL;" 2>/dev/null | sed 's/\t/,/g';)
if [ ! -z "${avgdata}" ]; then
  echo "vm_spawn_avg_time timediffinsec=${avgdata}"
fi

