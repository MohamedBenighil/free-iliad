# Free-Iliad : Old School Challenge

This example sets up 7 servers : 4 clikhouse and 3 keeper. The clickhouse instances runs 2 shards and 2 replicas. This deploy demonstrates use of files/template and splitting of tasks between different inventory groups. It looks like:

+ `inventories/docker.py` - inventory pointing at the Docker test containers
+ `deploy.py` - entrypoint/base package install
+ `tasks/clickhouse-keeper.py` - keeper servers setup
+ `tasks/clickhouse-server.py` - clickhouse servers setup

```sh
# Start Docker containers : infrastructure with 7 nodes
./docker-start.sh

# Run pyinfra against them 
pyinfra inventories/docker.py deploy.py

# P.S: If you get a set of errors like : SSH host key error (Host key for localhost does not match.) :
> ~/.ssh/known_hosts


# Ssh to one of clickhouse servers (clickhouse-01, clickhouse-02, clickhouse-03 or clickhouse-04)
ssh -i ./.docker/insecure_private_key pyinfra@localhost -p 9022 

# Run clickhouse client 
pyinfra@clickhouse-01:~$ clickhouse-client

# Check the cluster topologies
clickhouse-01 :) SELECT 
    cluster,
    shard_num,
    replica_num,
    host_name,
    port
FROM system.clusters;

   ┌─cluster────────────┬─shard_num─┬─replica_num─┬─host_name─────┬─port─┐
1. │ cluster_free_iliad │         1 │           1 │ clickhouse-01 │ 9000 │
2. │ cluster_free_iliad │         1 │           2 │ clickhouse-03 │ 9000 │
3. │ cluster_free_iliad │         2 │           1 │ clickhouse-02 │ 9000 │
4. │ cluster_free_iliad │         2 │           2 │ clickhouse-04 │ 9000 │
5. │ default            │         1 │           1 │ localhost     │ 9000 │
   └────────────────────┴───────────┴─────────────┴───────────────┴──────┘


# check the status of the ClickHouse Keeper cluster
clickhouse-01 :) SELECT *
FROM system.zookeeper
WHERE path IN ('/', '/clickhouse')

   ┌─name───────┬─value─┬─path────────┐
1. │ task_queue │       │ /clickhouse │
2. │ sessions   │       │ /clickhouse │
3. │ keeper     │       │ /           │
4. │ clickhouse │       │ /           │
   └────────────┴───────┴─────────────┘








###########################################
########### CREATE & QUERY DATA ########### 
###########################################

# create ReplicatedMergeTree table in 2 replicas (e.g: clickhouse-01 & clickhouse-03 OR clickhouse-02 & clickhouse-04 )
CREATE TABLE default.test_table
(
    id UInt64,
    name String
)
ENGINE = ReplicatedMergeTree(
    '/clickhouse/tables/cluster_free_iliad/01/test_table',  
    '{replica}' 
)
ORDER BY id; 


# Insert data (in one replicas: e.g: clickhouse-01 server)
INSERT INTO default.test_table VALUES (1, 'Mohamed01'), (2, 'Mohamed02');

# Read request from clickhouse-01
SELECT * FROM default.test_table;
   ┌─id─┬─name──────┐
1. │  1 │ Mohamed01 │
2. │  2 │ Mohamed02 │
   └────┴───────────┘

# Stop clickhouse-01 server


# Read request from clickhouse-03 server (You git the same result )
   ┌─id─┬─name──────┐
1. │  1 │ Mohamed01 │
2. │  2 │ Mohamed02 │
   └────┴───────────┘

# Delete Docker containers (infrastructure)
./docker-stop.sh
```
