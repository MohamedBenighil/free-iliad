#!/usr/bin/env bash

set -euo pipefail

source "$(realpath "$(realpath "$(dirname "${BASH_SOURCE[0]}")")/utils.sh")"

export DOCKER_TEST_NETWORK_NAME="free-iliad-network"

docker rm -f clickhouse-01
docker rm -f clickhouse-02
docker rm -f clickhouse-03
docker rm -f clickhouse-04
docker rm -f clickhouse-keeper-01
docker rm -f clickhouse-keeper-02
docker rm -f clickhouse-keeper-03


docker network rm "$DOCKER_TEST_NETWORK_NAME"
