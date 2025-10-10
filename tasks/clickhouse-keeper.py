
from pyinfra.operations import files, git, pip, server, systemd, apt


apt.packages(
    name="Installer le server ClickHouse keeper",
    packages=["clickhouse-keeper"],
    cache_time=3600,
)

# start the service clickhouse-server and enable it
systemd.service(
    name="Start & enable clickhouse-server.service",
    service="clickhouse-keeper.service",    
    running=True,
    enabled=True,
)
