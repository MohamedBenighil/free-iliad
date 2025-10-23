inventory = (
        # Individual host list with host-specific data
        [
            ("clickhouse-01.free-iliad.com", {"ssh_port": 9022, "is_clickHouse": True}),
            ("clickhouse-02.free-iliad.com", {"ssh_port": 9023, "is_clickHouse": True}),
            ("clickhouse-03.free-iliad.com", {"ssh_port": 9024, "is_clickHouse": True}),
            ("clickhouse-04.free-iliad.com", {"ssh_port": 9025, "is_clickHouse": True}),
            ("clickhouse-keeper-01.free-iliad.com", {"ssh_port": 9026, "is_clickHouseKeeper": True}),
            ("clickhouse-keeper-02.free-iliad.com", {"ssh_port": 9027, "is_clickHouseKeeper": True}),
            ("clickhouse-keeper-03.free-iliad.com", {"ssh_port": 9028, "is_clickHouseKeeper": True}),
        ],
        # Shared data for all the hosts in the group
        {
            "_sudo": True,  # use sudo for all operations
            # SSH details matching the Docker container started in ./docker-start.sh
            "ssh_hostname": "localhost",
            "ssh_user": "pyinfra",
            "ssh_key": "./.docker/insecure_private_key",
        },
    )
