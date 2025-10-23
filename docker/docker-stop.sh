#!/usr/bin/env bash

set -euo pipefail

source "$(realpath "$(realpath "$(dirname "${BASH_SOURCE[0]}")")/utils.sh")"

export DOCKER_TEST_NETWORK_NAME="free-iliad-network"

docker rm -f clickhouse-01.free-iliad.com
docker rm -f clickhouse-02.free-iliad.com
docker rm -f clickhouse-03.free-iliad.com
docker rm -f clickhouse-04.free-iliad.com
docker rm -f clickhouse-keeper-01.free-iliad.com
docker rm -f clickhouse-keeper-02.free-iliad.com
docker rm -f clickhouse-keeper-03.free-iliad.com


docker network rm "$DOCKER_TEST_NETWORK_NAME"
