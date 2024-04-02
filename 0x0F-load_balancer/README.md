# 0x0F Load Balancer

## Overview
This project includes scripts and configurations for setting up a load balancer for web servers. The goal is to distribute traffic between multiple web servers to improve reliability and performance.

## Description
The load balancer is configured to distribute incoming HTTP traffic between two web servers. This setup enhances the infrastructure's fault tolerance and load handling capabilities.

## Files
- 0-custom_http_response_header: Bash script to configure Nginx with a custom header on a new Ubuntu machine.
- 1-install_load_balancer: Bash script to install and configure HAproxy on a new Ubuntu machine.

## Setup and Configuration
To use the scripts, clone this repository and navigate to the 0x0F-load_balancer directory. Ensure the scripts have executable permissions:

\`\`\`bash
chmod +x 0-custom_http_response_header 1-install_load_balancer
\`\`\`

## Usage
To configure the Nginx servers with the custom header, run:

\`\`\`bash
./0-custom_http_response_header
\`\`\`

To install and configure HAproxy, run:

\`\`\`bash
./1-install_load_balancer
\`\`\`

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
