class CategoryTree
  attr_accessor :category, :parent, :nodes, :children

  def initialize
    @nodes = {}
  end
  
  def add_category(category, parent)
    if parent && !@nodes.values.join.include?(parent)
      raise ArgumentError
    end
    for node, childs in @nodes do
      if childs.include? category
        raise ArgumentError
      end
    end
    
    if nodes[parent].nil?
      nodes[parent] = []
    end

    @nodes[parent] << category

  end
    
  def get_children(category)
    nodes[category]
  end

end


c = CategoryTree.new
c.add_category('A', nil)
puts c.nodes
c.add_category('B', 'A')
puts c.nodes
c.add_category('C', 'A')
puts c.nodes
c.add_category('D', 'A')
puts c.nodes
c.add_category('E', 'D')
puts c.nodes
puts (c.get_children('A') || []).join(',')
