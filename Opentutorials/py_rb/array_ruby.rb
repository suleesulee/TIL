arr = ['a', 'b', 'c']
arr.each(){|i| puts i}

for value in arr
  puts value
end


arr2 = [1,3,56,7,13,52]
arr.delete_if() do |itme|
    item > 7
end
puts arr
