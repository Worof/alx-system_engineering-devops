#!/usr/bin/env bash
# This script configures Nginx to have a custom 404 page

# Create custom 404 page
echo "Ceci n'est pas une page" > /usr/share/nginx/html/404.html

# Configure Nginx to use the custom 404 page
echo 'server {
    listen 80;
    listen [::]:80;

    server_name _;

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }

    # Other server configurations...
}' > /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx restart
