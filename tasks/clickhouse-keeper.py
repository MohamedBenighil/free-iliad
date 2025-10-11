
from pyinfra.operations import files, git, pip, server, systemd, apt
from pyinfra import host
from pyinfra.facts.server import Hostname

apt.packages(
    name="Installer le server ClickHouse keeper",
    packages=["clickhouse-keeper"],
    cache_time=3600,
)

files.put(
    name="upload keeper_config.xml",
    src="templates/clickhouse-keeper/keeper_config.xml",
    dest="/etc/clickhouse-keeper/keeper_config.d/config.xml",
    user="clickhouse",
    group="clickhouse",
    create_remote_dir=True
)

systemd.service(
    name="Start & enable clickhouse-server.service",
    service="clickhouse-keeper.service",    
    running=True,
    enabled=True,
    # If we change the config.xml, restart it (if running already)
    # restarted=generate_unit.will_change,
)

generate_unit = files.line(
    name="Set unique server id",
    path="/etc/clickhouse-keeper/keeper_config.d/config.xml",
    line="<server_id></server_id>",
    # id = hostname's last 2 chars
    replace=f"<server_id>{host.get_fact(Hostname)[-2:]}</server_id>",
    
)


# # start the service clickhouse-server and enable it
# systemd.service(
#     name="Start & enable clickhouse-server.service",
#     service="clickhouse-keeper.service",    
#     running=True,
#     enabled=True,
#     # If we change the config.xml, restart it (if running already)
#     restarted=generate_unit.will_change,
# )
