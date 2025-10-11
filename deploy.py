from os import path

from pyinfra import host, local
from pyinfra.operations import apt, files, server
from pyinfra.facts.server import  Command



ARCH = host.get_fact(Command, "dpkg --print-architecture")

apt.packages(
    name="Installer les packages nécessaires pour les dépôts HTTPS",
    packages=["apt-transport-https", "ca-certificates", "curl", "gnupg"],
    cache_time=3600,
)


server.shell(
    name="Télécharger la clé GPG de ClickHouse",
    commands=[
        "curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' "
        "| gpg --dearmor | sudo tee /usr/share/keyrings/clickhouse-keyring.gpg > /dev/null"
    ],
)


clickhouse_repo_line = (
    f"deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg arch={ARCH}] "
    "https://packages.clickhouse.com/deb stable main"
)

apt.repo(
    name="Ajouter le dépôt ClickHouse dans apt sources",
    src=clickhouse_repo_line,
    filename="clickhouse",
)


apt.update(
    name="Mettre à jour la liste des packages apt",
    cache_time=3600,
)



if host.data.get("is_clickHouseKeeper"):
   local.include(filename=path.join("tasks", "clickhouse-keeper.py"))

if host.data.get("is_clickHouse"):
   local.include(filename=path.join("tasks", "clickhouse-server.py"))



