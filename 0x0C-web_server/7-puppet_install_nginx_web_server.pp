# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    listen [::]:80;

    server_name _;

    # Redirect /redirect_me to another page with a 301 status code
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    # Return "Hello World!" at root /
    location / {
        root /var/www/html;
        index index.html;
    }
}",
  require => Package['nginx'],
}

# Create "Hello World!" index page
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default', '/var/www/html/index.html'],
}
