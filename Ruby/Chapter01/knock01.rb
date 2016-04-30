# string is "パタトクカシーー".
# connect 1,3,5,7 character, and output its.


str = "パタトクカシーー"
sliced = ""

# print(str.length)
num = 0

0.step(str.length-1, 2) {|num|
  sliced += str[num]
}
puts(sliced)

