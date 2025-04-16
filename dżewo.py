import random

class Node():
    def __init__(self, value):
        self.value = value
        self.duplicates = 1
        self.big_child = None
        self.smol_child = None
    def add(self, new_child):
        if new_child.value > self.value:
            if self.big_child != None:
                self.big_child.add(new_child)
            else:
                self.big_child = new_child
        elif new_child.value < self.value:
            if self.smol_child != None:
                self.smol_child.add(new_child)
            else:
                self.smol_child = new_child
        else:
            self.duplicates +=1

            
    def search(self, the_value):
        if self.value == the_value:
            return True
        elif self.smol_child != None and self.value > the_value:
            return self.smol_child.search(the_value)
        elif self.big_child != None and self.value < the_value:
            return self.big_child.search(the_value)
        else:
            return False



    def draw_tree(self, prefix="", is_left=True):
        
        # Najpierw rysujemy prawe poddrzewo (żeby było "na górze")
        if self.smol_child is not None:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.smol_child.draw_tree(new_prefix, False)

        # Rysujemy bieżący węzeł
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(self.value))

        # Potem lewe poddrzewo (będzie "na dole")
        if self.big_child is not None:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.big_child.draw_tree(new_prefix, True)

    def twist_tree(self):
        self.big_child, self.smol_child = self.smol_child, self.big_child
        if self.big_child is not None:
            self.big_child.twist_tree()
        if self.smol_child is not None:
            self.smol_child.twist_tree()



    def count_leafs(self):
        w=0
        if self.big_child is not None:
            w+=self.big_child.count_leafs()
        if self.smol_child is not None:
            w+=self.smol_child.count_leafs()
        elif self.smol_child is None and self.big_child is None:
            w+=1
        return w
        


    def tree_height(self, height=1):
        maxheight = height
        performance = height
        if self.big_child is not None:
            maxheight = self.big_child.tree_height(height+1)
        if self.smol_child is not None:
            performance = self.smol_child.tree_height(height+1)
            if maxheight < performance:
                maxheight = performance
        return maxheight

random.seed(10)
elements = 200
root = Node(500)
for i in range(elements):
    random_number = random.randint(1, 1000)  
    root.add(Node(random_number))

print(root.search(random_number))

root.draw_tree()
root.twist_tree()
root.draw_tree()
print(f"LICZBA LIŚCI: {root.count_leafs()}")
print(F"WYSOKOŚĆ DRZEWA: {root.tree_height()}")
