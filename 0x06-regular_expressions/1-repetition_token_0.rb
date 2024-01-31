#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.length != 1
  puts "Usage: ./script_name.rb <string>"
  exit 1
end

# Get the input string
input_string = ARGV[0]

# Use a regular expression to match the pattern
matches = input_string.scan(/hb+t+n/)

# Print the matches
puts matches.join
