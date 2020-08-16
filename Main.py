class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

class Queue:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def update(self, index, value):
        counter = 0
        current_node = self.head
        if current_node != None:
            while current_node.next != None:
                if index == counter:
                    current_node.data = value
                    return
                current_node = current_node.next
                counter += 1
        if index == len(self.display()) - 1:
            self.tail.data = value
            return

    def enqueue(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            if self.size == 1:
                returnable = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return returnable.data
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
                self.size -= 1
                return next_node.data
        else:
            return "NULL"

    def getFirst(self):
        if self.size != 0:
            return self.head.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head == None and self.tail == None and self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = []
        current_node = self.head
        if current_node != None:
            while current_node.next != None:
                the_list.append(current_node.data)
                current_node = current_node.next
            the_list.append(self.tail.data)
        return the_list

class Max_Heap:
    def __init__(self):
        self.heap_list = []

    def insert(self, value):
        self.heap_list.append(value)
        self.shift_up(len(self.heap_list) - 1)

    def shift_up(self, node_index):
        parent_index = int((node_index - 1) / 2)
        if node_index != 0:
            if self.get_dedicated_number(self.heap_list[parent_index]) < self.get_dedicated_number(self.heap_list[node_index]):
                self.swap_indexes(parent_index, node_index)
                self.shift_up(parent_index)

    def swap_indexes(self, parent_index, node_index):
        temp = self.heap_list[parent_index]
        self.heap_list[parent_index] = self.heap_list[node_index]
        self.heap_list[node_index] = temp

    def display(self):
        return self.heap_list

    def delete(self):
        if len(self.heap_list) != 0:
            to_be_returned = self.heap_list[0]
            self.heap_list[0] = self.heap_list[len(self.heap_list) - 1]
            del self.heap_list[len(self.heap_list) - 1]
            self.shift_down(0)
            return to_be_returned
        else:
            print("LIST IS EMPTY !", len(self.heap_list))

    def clear(self):
        self.heap_list = []

    def shift_down(self, node_index):
        left_child_index = (2 * node_index) + 1
        right_child_index = (2 * node_index) + 2
        if left_child_index < len(self.heap_list) and right_child_index < len(self.heap_list):
            if self.get_dedicated_number(self.heap_list[left_child_index]) > self.get_dedicated_number(self.heap_list[right_child_index]):
                if self.get_dedicated_number(self.heap_list[left_child_index]) > self.get_dedicated_number(self.heap_list[node_index]):
                    self.swap_indexes(node_index, left_child_index)
                    self.shift_down(left_child_index)
            if self.get_dedicated_number(self.heap_list[left_child_index]) < self.get_dedicated_number(self.heap_list[right_child_index]):
                if self.get_dedicated_number(self.heap_list[right_child_index]) > self.get_dedicated_number(self.heap_list[node_index]):
                    self.swap_indexes(node_index, right_child_index)
                    self.shift_down(right_child_index)
            else:
                if self.get_dedicated_number(self.heap_list[left_child_index]) > self.get_dedicated_number(self.heap_list[node_index]):
                    self.swap_indexes(node_index, left_child_index)
                    self.shift_down(left_child_index)
        else:
            if left_child_index < len(self.heap_list):
                if self.get_dedicated_number(self.heap_list[left_child_index]) > self.get_dedicated_number(self.heap_list[node_index]):
                    self.swap_indexes(node_index, left_child_index)
            if right_child_index < len(self.heap_list):
                if self.get_dedicated_number(self.heap_list[right_child_index]) > self.get_dedicated_number(self.heap_list[node_index]):
                    self.swap_indexes(node_index, right_child_index)

    def get_dedicated_number(self, line):
        if line == "NULL":
            print("NULL came")
        line_parts = line.split("_")
        return int(line_parts[1])

    def get_dedicated_value(self, line):
        line_parts = line.split("_")
        return line_parts[0][0]

    def update_main_list(self, first_char, first_dedicated_number, second_char, second_dedicated_number, the_list):
        print(first_char, first_dedicated_number, second_char, second_dedicated_number, the_list, "update_main_list()")
        the_list[the_list.index(first_char + "_" + str(first_dedicated_number))] = first_char + "_" + str(second_dedicated_number)
        the_list[the_list.index(second_char + "_" + str(second_dedicated_number))] = second_char + "_" + str(first_dedicated_number)

    def swap_dedicated_numbers(self, first_char, deleting_times, second_char, second_dedicated_number, char_in_heap, the_list):
        print(first_char, deleting_times, second_char, second_dedicated_number, char_in_heap)
        self.update_main_list(first_char, deleting_times, second_char, second_dedicated_number, the_list)
        if char_in_heap is True:
            print(first_char + "_" + str(deleting_times), "is in ", main_heap.display())
            index_one = self.heap_list.index(first_char + "_" + str(deleting_times))
            index_two = len(main_queue.display()) - 1
            print(self.heap_list[index_one], main_queue.display()[index_two])
            self.heap_list[index_one] = second_char + "_" + str(deleting_times)
            main_queue.update(index_two, first_char + "_" + str(second_dedicated_number))
            print(self.heap_list[index_one], main_queue.display()[index_two])
        else:
            print(main_heap.display(), main_queue.display())
            print(first_char + "_" + str(deleting_times), "is not in", main_heap.display())
            index_one = main_queue.display().index(first_char + "_" + str(deleting_times))
            index_two = len(main_queue.display()) - 1
            print(main_queue.display()[index_one], main_queue.display()[index_two])
            main_queue.update(index_one, second_char + "_" + str(deleting_times))
            main_queue.update(index_two, first_char + "_" + str(second_dedicated_number))
            print(main_queue.display()[index_one], main_queue.display()[index_two])

    def swap_decoded(self, first_char, deleting_times, second_char, second_dedicated_number, the_list, the_heap, the_queue, num):
        print("cin >> HEAP :", the_heap.display(), "QUEUE :", the_queue.display(), num)
        self.update_main_list(first_char, deleting_times, second_char, second_dedicated_number, the_list)
        first_to_be = second_char + "_" + str(deleting_times)
        second_to_be = first_char + "_" + str(second_dedicated_number)
        if first_char + "_" + str(deleting_times) in the_queue.display():
            print(first_char + "_" + str(deleting_times), "FIRST IN QUEUE", first_to_be)
            the_queue.update(the_queue.display().index(first_char + "_" + str(deleting_times)), first_to_be)
        else:
            print(first_char + "_" + str(deleting_times), "FIRST IN HEAP", first_to_be)
            self.heap_list[the_heap.display().index(first_char + "_" + str(deleting_times))] = first_to_be
        if second_char + "_" + str(second_dedicated_number) in the_queue.display():
            print(second_char + "_" + str(second_dedicated_number), "SECOND IN QUEUE", second_to_be)
            the_queue.update(the_queue.display().index(second_char + "_" + str(second_dedicated_number)), second_to_be)
        else:
            print(second_char + "_" + str(second_dedicated_number), "SECOND IN HEAP", second_to_be)
            self.heap_list[the_heap.display().index(second_char + "_" + str(second_dedicated_number))] = second_to_be
        print("cout << HEAP :", the_heap.display(), "QUEUE :", the_queue.display(), num)

    def is_in_heap(self, number):
        searching_list = self.heap_list
        for each in searching_list:
            if self.get_dedicated_number(each) == number:
                return True
        return False


main_heap = Max_Heap()
main_queue = Queue()
main_list = []
encoded_msg = ""

def code(char):
    first = ""
    counter = 0
    for each in main_heap.display():
        if each[0] == char:
            first = each
            break
        counter += 1
    if first == "":
        counter = 0
        for each in main_queue.display():
            if each[0] == char:
                first = each
                break
            counter += 1
    first_parts = first.split("_")
    first_char = first[0][0]
    deleting_times = int(first_parts[1])
    if deleting_times > len(main_heap.display()):
        print("CAME", main_heap.display(), main_queue.display())
        print("---------------------------------------------------")
        for i in range(0, len(main_queue.display())):
            main_heap.insert(main_queue.dequeue())
            print(main_heap.display())
        print("---------------------------------------------------")
        print("GONE", main_heap.display(), main_queue.display())
    for i in range(0, deleting_times):
        main_queue.enqueue(main_heap.delete())
    second = str(main_queue.display()[len(main_queue.display()) - 1])
    second_parts = second.split("_")
    second_char = second_parts[0][0]
    second_dedicated_number = int(second_parts[1])
    main_heap.swap_dedicated_numbers(first_char, deleting_times, second_char, second_dedicated_number, True if first in main_heap.display() else False, main_list)
    if (first_char + "_" + str(second_dedicated_number)) in main_heap.display():
        main_heap.shift_up(main_heap.display().index(first_char + "_" + str(second_dedicated_number)))
    print("LIST :", main_list)
    print("HEAP :", main_heap.display())
    print("QUEUE :", main_queue.display())
    return second_char

def rebuild_max_heap_from_main_list():
    print(main_heap.display())
    main_heap.clear()
    print(main_heap.display(), "CLEARED")
    for each in main_list:
        main_heap.insert(each)
    print(main_heap.display(), "LETS GO")
    main_queue.clear()

def chain_to_array(chain):
    answer = []
    chain_parts = chain.split(" ")
    for each in chain_parts:
        answer.append(each)
    return answer

def chain_to_heap(chain):
    new_heap = Max_Heap()
    chain_parts = chain.split(" ")
    for each_part in chain_parts:
        new_heap.insert(each_part)
    return new_heap

def chain_to_queue(queue):
    new_queue = Queue()
    chain_parts = queue.split(" ")
    for each in chain_parts:
        new_queue.enqueue(each)
    return new_queue

def get_list_return_dedicated_number(given_list, char):
    for each in given_list:
        each_parts = each.split("_")
        if each_parts[0] == char:
            return int(each_parts[1])

def make_heap_from_array(given_list):
    new_heap = Max_Heap()
    for each in given_list:
        new_heap.insert(each)
    return new_heap

def make_queue_from_array(given_list):
    new_queue = Queue()
    for each in given_list:
        new_queue.enqueue(each)
    return new_queue

def decode(index, this_list, this_heap, this_queue, till_yet):
    temp_list = tuple(this_list)
    temp_heap = tuple(this_heap.display())
    temp_queue = tuple(this_queue.display())
    temp_till_yet = till_yet
    print("_", index, this_list, this_heap.display(), this_queue.display(), till_yet, "CAME !")
    # a_4 b_3 c_1 d_2
    if index == len(encoded_msg):
        print("===================================== ANSWER :", till_yet, "=============================================")
        return
    char = encoded_msg[index]
    if this_heap.is_in_heap(get_list_return_dedicated_number(this_list, char)) is True:
        # FIRST STAGE
        print(char, "FOUND IN HEAP")
        print("FIRST STAGE (", index, ") !", this_list, this_heap.display(), this_queue.display())
        counter = 0
        while True:
            deleted_root = this_heap.delete()
            this_queue.enqueue(deleted_root)
            counter += 1
            deleted_root_parts = deleted_root.split("_")
            deleted_root_char = deleted_root_parts[0][0]
            deleted_root_dedicated_number = int(deleted_root_parts[1])
            if deleted_root_char == char:
                for each in this_list:
                    parts = each.split("_")
                    if int(parts[1]) == counter:
                        answer = parts[0][0]
                        print("COUNTER", counter)
                        this_heap.swap_decoded(deleted_root_char, deleted_root_dedicated_number, answer, int(parts[1]), this_list, this_heap, this_queue, index)
                        print(this_list, this_heap.display(), this_queue.display(), "DONE", "CODED WITH :", answer)
                        till_yet += answer
                        decode(index + 1, this_list, this_heap, this_queue, till_yet)
                        break
                break
        # SECOND STAGE
        this_list = list(temp_list)
        this_heap = make_heap_from_array(list(temp_heap))
        this_queue = make_queue_from_array(list(temp_queue))
        if this_queue.getSize() != 0:
            till_yet = temp_till_yet
            print("SECOND STAGE (", index,") !", this_list, this_heap.display(), this_queue.display())
            for i in range(0, len(this_queue.display())):
                this_heap.insert(this_queue.dequeue())
            counter = 0
            while True:
                deleted_root = this_heap.delete()
                this_queue.enqueue(deleted_root)
                counter += 1
                deleted_root_parts = deleted_root.split("_")
                deleted_root_char = deleted_root_parts[0][0]
                deleted_root_dedicated_number = int(deleted_root_parts[1])
                if deleted_root_char == char:
                    for each in this_list:
                        parts = each.split("_")
                        if int(parts[1]) == counter:
                            answer = parts[0][0]
                            print("COUNTER", counter)
                            this_heap.swap_decoded(deleted_root_char, deleted_root_dedicated_number, answer, int(parts[1]), this_list, this_heap, this_queue, index)
                            print(this_list, this_heap.display(), this_queue.display(), "DONE", "CODED WITH :", answer)
                            till_yet += answer
                            decode(index + 1, this_list, this_heap, this_queue, till_yet)
                            break
                    break
        else:
            print("SECOND EMPTY !")
    else:
        print(char, index, "DIDN'T FOUND IN HEAP", this_list, this_heap.display(), this_queue.display())
        for i in range(0, len(this_queue.display())):
            this_heap.insert(this_queue.dequeue())
        counter = 0
        while True:
            deleted_root = this_heap.delete()
            this_queue.enqueue(deleted_root)
            counter += 1
            deleted_root_parts = deleted_root.split("_")
            deleted_root_char = deleted_root_parts[0][0]
            deleted_root_dedicated_number = int(deleted_root_parts[1])
            if deleted_root_char == char:
                for each in this_list:
                    parts = each.split("_")
                    if int(parts[1]) == counter:
                        answer = parts[0][0]
                        print("COUNTER", counter)
                        this_heap.swap_decoded(deleted_root_char, deleted_root_dedicated_number, answer, int(parts[1]), this_list, this_heap, this_queue, index)
                        print(this_list, this_heap.display(), this_queue.display(), "DONE", "CODED WITH :", answer)
                        till_yet += answer
                        decode(index + 1, this_list, this_heap, this_queue, till_yet)
                        break
                break


print("DS-PROJECT-THREE")
print("1- CODE", "2- DECODE 3- EXIT")
while True:
    order = int(input())
    if order == 1:
        print("Please enter the chain :")
        data_line = input()
        data_line_parts = data_line.split(" ")
        for each_part in data_line_parts:
            main_heap.insert(each_part)
            main_list.append(each_part)

        print(main_heap.display())
        print("Please enter the decoded Message which you want to encode :")
        to_be_coded_line = input()
        answer = []
        for each_char in to_be_coded_line:
            feedback = code(each_char)
            print("= " + feedback)
            answer.append(feedback)
        print("Answer :", "".join(answer))
    elif order == 2:
        print("Please enter the chain :")
        chain = input()
        print("Please enter the encoded Message which you want to decode :")
        encoded_msg = input()
        new_heap = chain_to_heap(chain)
        new_queue = Queue()
        new_queue.enqueue(0)
        new_queue.dequeue()
        decode(0, chain_to_array(chain), new_heap, new_queue, "")

        # data_line_parts = data_line.split(" ")
        # for each_part in data_line_parts:
        #     main_heap.insert(each_part)
        #     main_list.append(each_part)
        #
        # print(main_heap.display())
        # print("Please enter the encoded Message which you want to decode :")
        # to_be_coded_line = input()
        # answer = []
        # rebuild_max_heap_from_main_list()
        # for each_char in to_be_coded_line:
        #     feedback = decode(each_char)
        #     print("= " + feedback)
        #     answer.append(feedback)
        # print("Answer :", "".join(answer))

    elif order == 3:
        print("GOOD-BYE :)")
        break