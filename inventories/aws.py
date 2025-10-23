inventory = (
        # Individual host list with host-specific data
        [
            ("clickhouse-01.free-iliad.com", { "ssh_hostname": "clickhouse-01.free-iliad.com","is_clickHouse": True}),
            ("clickhouse-02.free-iliad.com", { "ssh_hostname": "clickhouse-02.free-iliad.com","is_clickHouse": True}),
            ("clickhouse-03.free-iliad.com", { "ssh_hostname": "clickhouse-03.free-iliad.com","is_clickHouse": True}),
            ("clickhouse-04.free-iliad.com", { "ssh_hostname": "clickhouse-04.free-iliad.com","is_clickHouse": True}),
            ("clickhouse-keeper-01.free-iliad.com", {"ssh_hostname": "clickhouse-keeper-01.free-iliad.com", "is_clickHouseKeeper": True}),
            ("clickhouse-keeper-02.free-iliad.com", {"ssh_hostname": "clickhouse-keeper-02.free-iliad.com", "is_clickHouseKeeper": True}),
            ("clickhouse-keeper-03.free-iliad.com", {"ssh_hostname": "clickhouse-keeper-03.free-iliad.com", "is_clickHouseKeeper": True}),
        ],
        # Shared data for all the hosts in the group
        {
            "_sudo": True,  # use sudo for all operations
            # SSH details matching the Docker container started in ./docker-start.sh
            "ssh_port": 22,
            "ssh_user": "ubuntu",
            "ssh_key": "./.ssh/insecure_private_key",
        },
    )
