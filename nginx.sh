#! /bin/bash

echo 'Nginx Running Directory'
echo $PWD

sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

sudo systemctl restart nginx

echo "Nginx status"

sudo systemctl status nginx