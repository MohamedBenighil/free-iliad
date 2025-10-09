inventory = (
    # Individual host list with host-specific data
    [
        ("host1", {"ssh_port": 9022, "is_clickHouse": True}),
        ("host2", {"ssh_port": 9023, "is_clickHouse": True}),
        ("host3", {"ssh_port": 9024, "is_clickHouse": True}),
        ("host4", {"ssh_port": 9025, "is_clickHouse": True}),
        ("host5", {"ssh_port": 9026, "is_keeper": True}),
        ("host6", {"ssh_port": 9027, "is_keeper": True}),
        ("host7", {"ssh_port": 9028, "is_keeper": True}),
    ],
    # Shared data for all the hosts in the group
    {
        "_sudo": True,  # use sudo for all operations
        # SSH details matching the Docker container started in ./docker-start.sh
        "ssh_hostname": "localhost",
        "ssh_user": "pyinfra",
        "ssh_key": "./.docker/insecure_private_key",
        # "ssh_known_hosts_file": "/dev/null",
        # This is insecure, don't use in production!
        # "ssh_strict_host_key_checking": "off",
    },
)


#insecure_private_key
#insecure_private_key.pub