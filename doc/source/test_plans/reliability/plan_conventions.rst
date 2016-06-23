- **OpenStack cluster:** consists of server nodes with deployed and fully
  operational OpenStack environment in high-availability configuration.

- **Fault-injection operation:** represents common types of failures which can
  occur in production environment: service-hang, service-crash,
  network-partition, network-flapping, and node-crash.

- **Service-hang:** faults are injected into specified OpenStack service by
  sending -SIGSTOP and -SIGCONT POSIX signals.

- **Service-crash:** faults are injected by sending -SIGKILL signal into
  specified OpenStack service.

- **Node-crash:** faults are injected to an OpenStack cluster by rebooting
  or shutting down a server node.

- **Network-partition:** faults are injected by inserting iptables rules to
  OpenStack cluster nodes to a corresponding service that should be
  network-partitioned.

- **Network-flapping:** faults are injected into OpenStack cluster nodes by
  inserting/deleting iptables rules on the fly which will affect
  corresponding service that should be tested.

- **Factor:** consists of a set of atomic fault-injection operations. For
  example: reboot-random-controller, reboot-random-rabbitmq.

- **Test plan:** contains two elements: test scenario
  execution graph and fault-injection factors.

- **SLA**: Service-level agreement

- **Testing-cycles**: number of test cycles of each factor

- **Inf**: assumes infinite time to auto-healing of cluster
  after fault-factor injection.
