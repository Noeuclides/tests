files = {"Input.txt"=>"Randy", "Code.py"=>"Stan", "Output.txt"=>"Randy"}
h = {}
for k, v in files do
  (h[v] ||=[]) << k
  puts h
end
  
