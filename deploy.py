from os import path

from pyinfra import host, local
from pyinfra.operations import apt, files, server
from pyinfra.facts.server import  Command



# Install prerequisite packages 
apt.packages(
    name="Installer les packages nécessaires pour les dépôts HTTPS",
    packages=["apt-transport-https", "ca-certificates", "curl", "gnupg"],
    # update=True,
    cache_time=3600,
)

# Download the ClickHouse GPG key and store it in the keyring
server.shell(
    name="Télécharger la clé GPG de ClickHouse",
    commands=[
        "curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' "
        "| gpg --dearmor | sudo tee /usr/share/keyrings/clickhouse-keyring.gpg > /dev/null"
    ],

)


ARCH = host.get_fact(Command, "dpkg --print-architecture")

clickhouse_repo_line = (
    f"deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg arch={ARCH}] "
    "https://packages.clickhouse.com/deb stable main"
)

# files.line(
#     name="Ajouter le dépôt ClickHouse dans apt sources",
#     path="/etc/apt/sources.list.d/clickhouse.list",
#     line=clickhouse_repo_line,
#     # create=True,
#     # present=False,
# )

apt.repo(
    name="Ajouter le dépôt ClickHouse dans apt sources",
    src=clickhouse_repo_line,
    filename="clickhouse",
)

# 5. Mettre à jour les paquets apt
apt.update(
    name="Mettre à jour la liste des paquets apt",
    cache_time=3600,
)



if host.data.get("is_clickHouse"):
   local.include(filename=path.join("tasks", "clickhouse-server.py"))

#
if host.data.get("is_clickHouseKeeper"):
   local.include(filename=path.join("tasks", "clickhouse-keeper.py"))
