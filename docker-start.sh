#!/usr/bin/env bash

set -euo pipefail

source "$(realpath "$(realpath "$(dirname "${BASH_SOURCE[0]}")")/utils.sh")"
ensure_test_container

export DOCKER_TEST_NETWORK_NAME="free-iliad-network"

echo "Create Docker network..."
docker network create "$DOCKER_TEST_NETWORK_NAME"

echo "Starting Docker containers..."
run_test_container clickhouse-01.free-iliad.com -p 9022:22
run_test_container clickhouse-02.free-iliad.com -p 9023:22
run_test_container clickhouse-03.free-iliad.com -p 9024:22
run_test_container clickhouse-04.free-iliad.com -p 9025:22
run_test_container clickhouse-keeper-01.free-iliad.com -p 9026:22
run_test_container clickhouse-keeper-02.free-iliad.com -p 9027:22
run_test_container clickhouse-keeper-03.free-iliad.com -p 9028:22

echo
echo "Doker containers are now ready to run the pyinfra deploy, you can do this by running:"
echo
echo "    pyinfra inventories/docker.py deploy.py"
echo
echo "Once complete, don't forget to remove the Docker containers and network using the ./docker-stop.sh script!"
