# 0x10-HTTPS_SSL

This directory contains the tasks for the "HTTPS SSL" project, part of the ALX Software Engineering program. The focus of this project is to understand and implement HTTPS and SSL configurations, emphasizing securing web traffic and understanding SSL termination.

## Project Overview

This project includes various tasks that deal with configuring HTTPS and SSL for web servers and load balancers. Learners will configure DNS records, set up HAproxy for SSL termination, and ensure all traffic is redirected from HTTP to HTTPS, enhancing the security of web communications.

## Learning Objectives

By the end of this project, learners should be able to:

- Explain the roles of HTTPS and SSL in securing web traffic.
- Configure DNS A records for domain and subdomains.
- Implement SSL termination with HAproxy.
- Redirect HTTP traffic to HTTPS automatically.

## Files and Descriptions

- `0-world_wide_web`: A script that configures domain zones and subdomains, then displays information about these domains.
- `1-haproxy_ssl_termination`: Configuration files and scripts used to set up HAproxy for SSL termination.
- `100-redirect_http_to_https`: Scripts and configuration files to enforce the redirection of HTTP traffic to HTTPS.

## Setup and Usage

### Configuring DNS Records

- Modify the DNS settings for your domain to add A records for `www`, `lb-01`, `web-01`, and `web-02`, pointing to their respective IP addresses.

### HAproxy SSL Termination

- Ensure that HAproxy is installed and running.
- Use the provided scripts and configuration snippets to set up SSL termination on HAproxy.

### Redirecting HTTP to HTTPS

- Adjust the HAproxy configuration to redirect HTTP traffic to HTTPS, ensuring secure communication.

## Testing

After configuring the services, you can test the setup using `curl` or a web browser to ensure that the configurations are working as expected.

## Contributions

This project is part of the ALX curriculum. Contributions, bug reports, and suggestions are welcome.
