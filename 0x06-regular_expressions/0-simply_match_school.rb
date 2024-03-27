#!/usr/bin/env ruby
# Check if an argument was provided
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit 1
end

# Get the input string
input_string = ARGV[0]

# Use a regular expression to match "School"
matches = input_string.scan(/School/)

# Print the matches
puts matches.join
