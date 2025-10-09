#!/usr/bin/env bash

set -euo pipefail

source "$(realpath "$(realpath "$(dirname "${BASH_SOURCE[0]}")")/utils.sh")"

export DOCKER_TEST_NETWORK_NAME="pyinfra-examples-python-web-app"

docker rm -f host1
docker rm -f host2
docker rm -f host3
docker rm -f host4
docker rm -f host5
docker rm -f host6
docker rm -f host7

docker network rm "$DOCKER_TEST_NETWORK_NAME"
