#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
  puts "Please provide a string to match."
  exit
end

# The input string from the user
input_string = ARGV[0]

# Regular expression pattern to match only capital letters
pattern = /[A-Z]/

# Find all capital letters in the input string
matches = input_string.scan(pattern)

# Join the matches into a single string
result = matches.join

# Print the result
puts result
