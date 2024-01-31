#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
  puts "Please provide a string to match."
  exit
end

# The input string from the user
input_string = ARGV[0]

# Regular expression pattern to match 'hb+t+n'
pattern = /hb+t+n/

# Check if the input string matches the pattern
if input_string.match?(pattern)
  puts "The string matches the pattern."
else
  puts "The string does not match the pattern."
end
