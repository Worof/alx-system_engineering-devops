# 2-execute_a_command.pp
# This manifest uses the exec resource to kill a process named killmenow using pkill

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
