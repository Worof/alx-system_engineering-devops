# 1-install_a_package.pp
# This manifest installs Flask version 2.1.0 using pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
