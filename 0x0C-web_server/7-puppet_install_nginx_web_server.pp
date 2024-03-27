#!/usr/bin/env bash

class nginx_setup {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('modulename/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  exec { 'reload_nginx':
    command     => '/usr/sbin/nginx -s reload',
    refreshonly => true,
  }
}

include nginx_setup
