class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"


class UpdatedLL(LinkedList):
    def __init__(self):
        super().__init__()

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def len_ll(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def insert_at_index(self, data, index):
        new_node = Node(data)
        ll_length = self.len_ll()
        if ll_length >= index:
            if index == 0:
                self.insert_at_head(data)
            else:
                current_index = 0
                current_node = self.head
                while current_node is not None:
                    if index == current_index:
                        new_node.prev_node = current_node.prev_node
                        current_node.prev_node.next_node = new_node
                        current_node.prev_node = new_node
                        new_node.next_node = current_node
                        return "Done"
                    current_index += 1
                    current_node = current_node.next_node
        else:
            return "Out of range"

    def remove_node_index(self, index):
        ll_length = self.len_ll()
        if ll_length >= index:
            if index == 0:
                self.remove_from_head()
            elif index == ll_length - 1:
                self.remove_from_tail()
            else:
                current_index = 0
                current_node = self.head
                while current_node is not None:
                    if index == current_index:
                        current_node.prev_node.next_node = current_node.next_node
                        current_node.next_node.prev_node = current_node.prev_node
                        return "Done"
                    current_index += 1
                    current_node = current_node.next_node
        else:
            return "Out of range"

    def __contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next_node
        return False

    def __contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.prev_node
        return False

    def contains_from(self, data, method="head"):
        if method == "head":
            return self.__contains_from_head(data)
        elif method == "tail":
            return self.__contains_from_tail(data)
        else:
            return 'Метод должен быть либо "head", либо "tail"'

    def remove_node_data(self, data):
        if self.contains_from(data):
            current_index = 0
            current_node = self.head
            while current_node is not None:
                if current_node.data == data:
                    self.remove_node_index(current_index)
                else:
                    current_index += 1
                    current_node = current_node.next_node
        else:
            return 'data не найдена'
