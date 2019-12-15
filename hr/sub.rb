def split_word s
  a = (0..s.length).inject([]){|ai,i|
    (1..s.length - i).inject(ai){|aj,j|
      aj << s[i,j]
    }
  }.uniq
  puts a
end
