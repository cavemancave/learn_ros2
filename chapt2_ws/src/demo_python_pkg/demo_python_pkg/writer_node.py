from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, name_value, age_value, book:str):
        print('WriterNode __init__ ')
        super().__init__(name_value, age_value)
        self.book = book

def main():
    node = WriterNode('张三', 18, '刑法')
    node.eat('鱼香肉丝')