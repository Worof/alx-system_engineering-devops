# 100-puppet_ssh_config.pp
# This manifest configures SSH client to use a specific private key and disable password authentication

# Ensure the private key is declared in the SSH config
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
  ensure => present,
}

# Ensure that password authentication is turned off
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  ensure => present,
}
