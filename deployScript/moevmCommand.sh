#!/bin/bash
# Скрипт для развертывания кафедральных приложений
# use option -d without arguments clear database
# use option -f without arguments add fake data to data base
# use option -i without arguments install app with requirements
# use option -u without arguments update app
# use option -c <catalog_name> to project
# use option -s <server_name> to set server name
# use option -r <error_log_name> to using new apache error log name

CATALOG='moevmApps'
DATABASE_NAME = 'moevmApps'
ERROR_LOG_NAME='error'
SERVER_NAME='moevmApps'
SERVER_PORT='80'
HOSTS_STRING="127.0.0.1"
DEBUG_FILE="/var/www/moevmApps/DEBUG"
CONFIG_FILE="moevmApps.conf"
MONGO_INSTALL_DIR = "/var/lib/mongodb"
FLAG_CLEAR_DB=false
FLAG_INSTALL_APP=false
FLAG_UPDATE_APP=false
FLAG_ADD_FAKE_DATA=false


while getopts ":d:f:i:c:s:r:u" opt ;
do
    case $opt in
        d) FLAG_CLEAR_DB=true;
            ;;
        f) FLAG_ADD_FAKE_DATA=true;
            ;;
        i) FLAG_INSTALL_APP=true;
            ;;
        c) CATALOG=$OPTARG;
            ;;
        s) SERVER_NAME=$OPTARG;
            ;;
        r) ERROR_LOG_NAME=$OPTARG;
            ;;
        u) FLAG_UPDATE_APP=true;
            ;;
        *) echo "the option is incorrect";
            exit 1
            ;;
        esac
done

# install app
if $FLAG_INSTALL_APP
then
    # install mongo
	curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.2.10.tgz
	tar -zxvf mongodb-linux-x86_64-3.2.10.tgz
	mkdir -p mongodb
    cp -R -n mongodb-linux-x86_64-3.2.10/ mongodb
    mv mongodb MONGO_INSTALL_DIR
    export PATH=MONGO_INSTALL_DIR/bin:$PATH
    rm mongodb-linux-x86_64-3.2.10.tgz
    rm -r mongodb-linux-x86_64-3.2.10
    # install pip requirements
    pip install git+https://github.com/django-nonrel/django@nonrel-1.5
    pip install git+https://github.com/django-nonrel/djangotoolbox
    pip install git+https://github.com/django-nonrel/mongodb-engine

    # install pip projects.
    pip install git+https://github.com/w3prog/moevmCommon
    pip install git+https://github.com/w3prog/teacherPlan
    pip install git+https://github.com/EvgeniyGor/StudentRecords
    pip install git+https://github.com/dartl/IS_ScientificWork

fi

# update app
if $FLAG_UPDATE_APP
then
    # install pip projects.
    pip install git+https://github.com/w3prog/moevmCommon --upgrade
    pip install git+https://github.com/w3prog/teacherPlan --upgrade
    pip install git+https://github.com/EvgeniyGor/StudentRecords --upgrade
    pip install git+https://github.com/dartl/IS_ScientificWork --upgrade

fi

# reinstall database
if $FLAG_CLEAR_DB
then
    mongo $DATABASE_NAME --eval "db.dropDatabase()"
fi

# add some fake data
if $FLAG_ADD_FAKE_DATA
then
    pythom manage.py seedfakedata
fi