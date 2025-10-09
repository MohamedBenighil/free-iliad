#!/usr/bin/env bash

set -euo pipefail

source "$(realpath "$(realpath "$(dirname "${BASH_SOURCE[0]}")")/utils.sh")"
ensure_test_container

export DOCKER_TEST_NETWORK_NAME="pyinfra-examples-python-web-app"

echo "Create Docker network..."
docker network create "$DOCKER_TEST_NETWORK_NAME"

echo "Starting Docker containers..."
run_test_container host1 -p 9022:22
run_test_container host2 -p 9023:22
run_test_container host3 -p 9024:22
run_test_container host4 -p 9025:22
run_test_container host5 -p 9026:22
run_test_container host6 -p 9027:22
run_test_container host7 -p 9028:22

echo
echo "Doker containers are now ready to run the pyinfra deploy, you can do this by running:"
echo
echo "    pyinfra inventories/docker.py deploy.py"
echo
echo "Once complete, don't forget to remove the Docker containers and network using the ./docker-stop.sh script!"
