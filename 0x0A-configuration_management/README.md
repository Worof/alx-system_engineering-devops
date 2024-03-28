# 0x0A Configuration Management

This directory is dedicated to the practice and implementation of configuration management using Puppet. The exercises here are designed to provide hands-on experience with Puppet's basic functionalities, including creating files, installing packages, and executing commands.

## Overview

The tasks in this directory are focused on using Puppet manifests to automate the configuration of servers. These manifests ensure that certain conditions are met on the servers they are applied to, such as ensuring specific files exist, packages are installed, or services are running.

## Prerequisites

- Ubuntu 20.04 LTS
- Puppet 5.5
- puppet-lint 2.1.1

Ensure that your environment is set up with the above specifications to correctly execute the Puppet manifests in this directory.

## Files in This Directory

- **0-create_a_file.pp**: A Puppet manifest that creates a file at `/tmp/school` with specific content, owner, group, and permissions.
- **[Additional Puppet Manifests]**: Other `.pp` files in the directory should be documented similarly, describing their purpose and functionality.

## Usage

To apply a Puppet manifest, navigate to this directory in your terminal and run:

```bash
puppet apply [filename].pp
