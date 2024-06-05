# 0-strace_is_your_friend.pp
# Fix permissions on the WordPress directory
file { '/var/www/html/wp-content':
    ensure => 'directory',
    owner  => 'www-data',
    group  => 'www-data',
    mode   => '0755',
    recurse => true,
    notify  => Service['apache2'],
}

# Ensure Apache is always running
service { 'apache2':
    ensure     => running,
    enable     => true,
    subscribe  => File['/var/www/html/wp-content'],
}
