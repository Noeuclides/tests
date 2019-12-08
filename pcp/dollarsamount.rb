class Bank
  def least_number_of_dollars(dollars, amount)
    i = 0
    count = 0
    change = dollars.reverse
    while i < change.length do
      puts change[i]
      if amount/change[i] >= 1
        amount = amount - change[i]
        count = count + 1
      else
        i = i + 1
      end
    end
    return count
  end
end

b = Bank.new
puts b.least_number_of_dollars([1,2,5], 11)
