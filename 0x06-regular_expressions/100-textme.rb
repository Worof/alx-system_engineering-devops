#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
  puts "Please provide a string to match."
  exit
end

# The input string from the user
input_string = ARGV[0]

# Regular expression pattern to match sender, receiver, and flags
pattern = /\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/

# Check if the input string matches the pattern
match_data = input_string.match(pattern)

# If the input string matches the pattern, print the sender, receiver, and flags
if match_data
  sender, receiver, flags = match_data.captures
  puts "#{sender},#{receiver},#{flags}"
else
  puts "The string does not match the pattern."
end
