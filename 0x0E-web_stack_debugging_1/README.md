# 0x0E-Web Stack Debugging #1

This project is part of the ALX System Engineering DevOps track. It focuses on the fundamental concepts of web stack debugging, specifically targeting Nginx running on an Ubuntu server. The main goal is to develop skills in debugging issues related to Nginx not listening on the expected port, which is port 80 in this case.

## Description

In this project, students are tasked with diagnosing and resolving an issue where an Nginx server is not listening on port 80 as expected. Through this exercise, students will gain hands-on experience with common debugging tools and techniques in a controlled environment.

## Objectives

- Understand the basics of web stack debugging
- Diagnose why Nginx is not listening on port 80
- Develop a Bash script to automate the debugging and resolution process
- Apply best practices in writing Bash scripts
- Use version control with Git

## Requirements

- All files should be executed on Ubuntu 20.04 LTS using `bash`
- All Bash script files must be executable
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's functionality
- Do not use `wget`
- All your files should end with a new line

## Tasks

### 0. Nginx likes port 80

Write a Bash script that configures a server to listen on port 80. The script should ensure that Nginx is running and listening on all active IPv4 IPs on the server.

Filename: `0-nginx_likes_port_80`

### 1. Make it sweet and short (Advanced Task)

Optimize the script from task 0 to be 5 lines long or less, adhering to all script requirements mentioned above.

Filename: `1-debugging_made_short`

## Usage

To use the debugging scripts, clone the repository, navigate to the `0x0E-web_stack_debugging_1` directory, and execute the scripts as follows:

```bash
./0-nginx_likes_port_80
