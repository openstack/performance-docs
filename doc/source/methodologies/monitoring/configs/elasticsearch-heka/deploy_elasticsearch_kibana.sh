#!/bin/bash -xe

HOSTNAME=`hostname`
ELASTICSEARCH_NODE=${ELASTICSEARCH_NODE:-172.20.9.3}

# install java
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y install oracle-java8-installer

# install elastic by adding extra repository
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
sudo apt-get update
sudo apt-get -y install elasticsearch

# edit configuration:
sed -i -E -e 's/^.*cluster.name: .*$/ cluster.name: elasticsearch_k8s/g' /etc/elasticsearch/elasticsearch.yml
sed -i -E -e "s/^.*node.name: .*$/ cluster.name: ${HOSTNAME}/g" /etc/elasticsearch/elasticsearch.yml
sed -i -E -e "s/^.*network.host: .*$/ network.host: ${ELASTICSEARCH_NODE}/g" /etc/elasticsearch/elasticsearch.yml

# increase memory limits:
sed -i -E -e "s/^.*ES_HEAP_SIZE=.*$/ES_HEAP_SIZE=10g/g" /etc/default/elasticsearch

# start service:
sudo systemctl restart elasticsearch
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch

# install kibana from extra repository:
echo "deb http://packages.elastic.co/kibana/4.5/debian stable main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get -y install kibana
sed -i -E -e "s/^.*elasticsearch.url:.*$/ elasticsearch.url: \"http://${ELASTICSEARCH_NODE}:9200\"/g" /opt/kibana/config/kibana.yml

# enable kibana service:
sudo systemctl daemon-reload
sudo systemctl enable kibana
sudo systemctl start kibana

# install nginx:
sudo apt-get -y install nginx

# set kibana admin:password (admin:admin)
echo "admin:`openssl passwd admin`" | sudo tee -a /etc/nginx/htpasswd.users

# prepare nginx config:
cat << EOF >> /etc/nginx/sites-available/default
server {
    listen 80;

    server_name ${HOSTNAME};

    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/htpasswd.users;

    location / {
        proxy_pass http://localhost:5601;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }
}
EOF

# check and start nginx service:
sudo nginx -t
sudo systemctl restart nginx

