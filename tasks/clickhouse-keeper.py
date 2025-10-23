
from pyinfra.operations import files, systemd, apt
from pyinfra import host


apt.packages(
    name="Install clickhouse-keeper",
    packages=["clickhouse-keeper"],
    cache_time=3600,
)

generate_unit =files.put(
    name="Upload common config file",
    src="templates/clickhouse-keeper/keeper_config.xml",
    dest="/etc/clickhouse-keeper/keeper_config.d/config.xml",
    user="clickhouse",
    group="clickhouse",
    create_remote_dir=True
)

generate_unit = files.line(
    name="Set specific config : Set unique server id",
    path="/etc/clickhouse-keeper/keeper_config.d/config.xml",
    line="<server_id></server_id>",
    # id = hostname's  2 number
    replace=f"<server_id>{host.name.split('.')[0][-2:]}</server_id>",
)

systemd.service(
    name="Start & enable clickhouse-keeper.service",
    service="clickhouse-keeper.service",    
    running=True,
    enabled=True,
    restarted=generate_unit.will_change,
)
