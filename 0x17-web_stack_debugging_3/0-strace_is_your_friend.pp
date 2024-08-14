# 0-strace_is_your_friend.pp
# Fix file permissions for WordPress
file { '/var/www/html/wp-config.php':
  ensure => 'file',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}
