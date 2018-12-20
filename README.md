# blkplt

## RocksDB

#### Installation

```
# installs the apt-add-repository command
apt-get install -y software-properties-common

# installs java
apt-add-repository ppa:webupd8team/java
apt update
apt install -y oracle-java8-installer

# installs maven
apt install -y maven

# builds installs YCSB
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB
mvn clean package
```


#### Experiment

```
./bin/ycsb load rocksdb -P workloads/workloada -p rocksdb.dir=~/mnt -p recordcount=250000000 -p operationcount=500000000 -s -threads 16
./bin/ycsb run rocksdb -P workloads/workloada -p rocksdb.dir=~/mnt -p recordcount=250000000 -p operationcount=500000000 -s -threads 16

-P
    select a default work load, in this case workloads/workloada

-p
    specify some custom parameters for the workload
    - rocksdb.dir=~/mnt  # the directory to use for RocksDB
    - recordcount=250000000  # the number of records in RocksDB
    - operationount=250000000  # the number of operations to perform

-s
    print the progress out to stderr

-threads
    the number of client threads writing to RocksDB, in this case 16
```
