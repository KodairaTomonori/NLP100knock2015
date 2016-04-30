# str1 = "パトカー", str2 = "タクシー"
# alternately connect str1 and str2 : = "パタトクカシーー"


str1, str2 = "パトカー", "タクシー"
connected = ""

0.upto(str1.length - 1) {|num|
  connected += str1[num] + str2[num]
}
puts(connected)
