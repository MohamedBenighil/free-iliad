from pyinfra.operations import files, git, pip, server, systemd, apt
from pyinfra import host

apt.packages(
    name="Installer le server ClickHouse  et le client",
    packages=["clickhouse-server", "clickhouse-client"],
    cache_time=3600,
)


generate_unit = files.put(
    name="upload common config.xml",
    src="templates/clickhouse-server/config.xml",
    dest="/etc/clickhouse-server/config.d/config.xml",
    user="clickhouse",
    group="clickhouse",
    
)

generate_unit = files.put(
        name=f"Upload a specific config for {host.name}",
        src=f"templates/clickhouse-server/{host.name}.xml",
        dest=f"/etc/clickhouse-server/config.d/{host.name}.xml",
        user="clickhouse",
        group="clickhouse",
    )

systemd.service(
    name="Start & enable clickhouse-server.service",
    service="clickhouse-server.service",
    running=True,
    enabled=True,
    restarted=generate_unit.will_change,
)
