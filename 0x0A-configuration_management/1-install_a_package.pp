<<<<<<< HEAD
# Puppet manifest to install flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
=======
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
>>>>>>> 3cf5b76265a5062a2865cdd4a1d660e64ca7c9e0
}
