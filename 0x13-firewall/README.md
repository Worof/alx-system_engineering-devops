# 0x13-Firewall

## Overview

This directory contains scripts and configuration files for setting up and managing firewall rules using UFW (Uncomplicated Firewall) on Linux servers. The primary goal is to enhance security by controlling the inbound and outbound traffic to the servers.

## Contents

- **0-block_all_incoming_traffic_but**: This script configures UFW to deny all incoming traffic except for traffic on specific ports. It allows traffic on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS). This ensures the server can still be accessed via standard protocols while keeping it secure from unwanted access.

- **100-port_forwarding**: This configuration file includes settings to redirect incoming traffic on port 8080 to port 80. This is useful for applications that need to run on alternate ports but should be accessible from standard HTTP ports.

## Installation and Setup

1. **Installing UFW:**
   - Update your package list: `sudo apt update`
   - Install UFW: `sudo apt install ufw`

2. **Setting Up Firewall Rules:**
   - Navigate to the directory containing the scripts: `cd 0x13-firewall`
   - Run the setup script to apply firewall rules: `sudo ./0-block_all_incoming_traffic_but`

3. **Enabling Port Forwarding (if required):**
   - Ensure that IP forwarding is enabled on your server by editing `/etc/ufw/sysctl.conf` and uncommenting:
     ```
     net.ipv4.ip_forward=1
     net.ipv6.conf.all.forwarding=1
     ```
   - Apply port forwarding rules as specified in `100-port_forwarding`.

## Usage

To check the status of UFW and view currently applied rules, use:
```bash
sudo ufw status verbose

