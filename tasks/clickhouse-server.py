from pyinfra.operations import files, git, pip, server, systemd, apt

apt.packages(
    name="Installer le server ClickHouse  et le client",
    packages=["clickhouse-server", "clickhouse-client"],
    cache_time=3600,
)

# start the service clickhouse-server and enable it
# systemd.service(
#     name="Start & enable clickhouse-server.service",
#     service="clickhouse-server.service",
#     running=True,
#     enabled=True,
# )


generate_unit = files.template(
    name="override config.xml pour créer un cluster",
    src="templates/clickhouse-server/config.xml",
    dest="/etc/clickhouse-server/config.d/config.xml",
)

systemd.service(
    name="Start & enable clickhouse-server.service",
    service="clickhouse-server.service",
    running=True,
    enabled=True,
    # If we change the config.xml, restart it (if running already)
    restarted=generate_unit.will_change,
)
