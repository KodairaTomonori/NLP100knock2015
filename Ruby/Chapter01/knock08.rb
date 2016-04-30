# make cipher function
# - if character is lower, replace to (219 - character code)
# - else output as it is
# Using cipher function, decode/encode English message.


def cipher(string)
  0.upto(string.length-1){|n|
    if string[n].match(/[a-z]/)
      string[n] = (219 - string[n].ord).chr
    end
  }
  return string 
end

orig = "abcD_Wxyz"
puts "original: " + orig
encoded = cipher(orig)
puts "encoded:  " + encoded
decoded = cipher(encoded)
puts "decoded:  " + decoded
