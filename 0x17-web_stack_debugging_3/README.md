# Web Stack Debugging #3

## Project Overview
This project involves debugging a Wordpress website running on a LAMP stack that is currently returning a 500 Internal Server Error. The goal is to identify the source of the error using `strace` and then automate the fix using Puppet.

## Objectives

- Use `strace` to identify why Apache is returning a 500 error.
- Automate the solutions using Puppet instead of Bash scripts.

## Tools Used

- `strace` for debugging and identifying system calls that fail.
- Puppet for configuration management and automating the deployment of fixes.

## Debugging Steps

1. Attach `strace` to the Apache process.
2. Analyze the output to identify errors such as permission issues, missing files, or misconfigurations.
3. Create a Puppet manifest to address these issues.

## Puppet Manifest

- `0-strace_is_your_friend.pp`: Contains the Puppet code that fixes the identified issues.

## Usage

To apply the Puppet manifest, run:

```bash
sudo puppet apply 0-strace_is_your_friend.pp
