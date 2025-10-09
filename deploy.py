from os import path

from pyinfra import host, local
from pyinfra.operations import apt, files, git, pip, server, systemd


# Install prerequisite packages 
apt.packages(
    name="Installer les packages nécessaires pour les dépôts HTTPS",
    packages=["apt-transport-https", "ca-certificates", "curl", "gnupg"],
    update=True,
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


arch_result = server.shell(
    name="Récupérer l'architecture système",
    commands=["dpkg --print-architecture"],
    get_stdout=True,
)

ARCH = arch_result.stdout[0] if arch_result.stdout else "amd64"  # fallback


clickhouse_repo_line = (
    f"deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg arch={ARCH}] "
    "https://packages.clickhouse.com/deb stable main"
)

files.line(
    name="Ajouter le dépôt ClickHouse dans apt sources",
    path="/etc/apt/sources.list.d/clickhouse.list",
    line=clickhouse_repo_line,
    create=True,
)

# 5. Mettre à jour les paquets apt
apt.update(
    name="Mettre à jour la liste des paquets apt",
)



#if host.data.get("is_database"):
#    local.include(filename=path.join("tasks", "database.py"))
#
#
#if host.data.get("is_web"):
#    local.include(filename=path.join("tasks", "web.py"))
