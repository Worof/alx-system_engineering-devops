#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
  puts "Please provide a string to match."
  exit
end

# The input string from the user
input_string = ARGV[0]

# Regular expression pattern to match a 10 digit phone number
pattern = /^\d{10}$/

# Check if the input string matches the pattern
if input_string.match?(pattern)
  puts "#{input_string} matches the regular expression."
else
  puts "#{input_string} does not match the regular expression."
end
