import itertools # ex4()
import time


# DONE
def ex1 (numbers: list[int]=[-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]) -> tuple[int, int]:
    """Count positive and negative numbers in a list"""
    pos_count = sum(1 for n in numbers if n > 0)
    neg_count = sum(1 for n in numbers if n < 0)

    return pos_count, neg_count


# DONE
def ex2 (f: int=3, numbers: list[int]=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]) -> list[int]:
    """Extract all elements from a list whose frequency is greater than f."""
    out = []
    for n in numbers:
        if numbers.count(n) > f and n not in out:
            out.append(n)

    return out


# DONE
def ex3(numbers=[4, 5, 6, 7, 3, 9, 11, 2, 10]):
    """Find the strongest neighbour.

    Given a list of N positive integers find the maximum for every adjacent pair in the array.
    """
    strongest_neighbors = []
    for i, n in enumerate(numbers[:-1]):
        if n > numbers[i + 1]:
            strongest_neighbors.append(n)
        else:
            strongest_neighbors.append(numbers[i + 1])

    return strongest_neighbors


# DONE
def ex4 (numbers: list[int]=[1, 2, 3]) -> str:
    """Find all Possible Combinations from a list of Digits"""
    out = []
    for n in range(len(numbers) + 1):
        combinations = list(itertools.combinations(numbers, n))
        out.append(f"combo of {n}: {combinations}")

    return out


# DONE
def ex5 (m1: list[list[int]]=[[4, 3, 5], [1, 2, 3], [3, 7, 4]], m2: list[list[int]]=[[1, 3], [9, 3, 5, 7], [8]]) -> list[list[int]]:
    """Add two matrices."""
    for i, lst in enumerate(m2):
        while lst:
            m1[i].append(lst.pop(0))

    return m1


# DONE
def ex6 (lower_limit: int=2000, upper_limit: int=3200) -> str:
    """Find all numbers in a range which are divisible by 7 but not by 5"""
    ll = lower_limit
    while not ll % 7 == 0:
        ll += 1

    out = []
    for n in range(ll, upper_limit+1, 7):
        if not n % 5 == 0:
            out.append(str(n))

    return ", ".join(out)


# DONE
def ex7 (lower_limit: int=1000, upper_limit: int=3000) -> str:
    """Find all numbers where each digit of the number is an even digit."""
    even_numbers = "02468"
    out = []
    for n in range(lower_limit, upper_limit+1):
        if all(digit in even_numbers for digit in str(n)):
            out.append(str(n))

    return ", ".join(out)


class Node:
    def __init__(self, data: str):
        self.data = data
        self.w_beg = data[:2]
        self.w_end = data[-2:]
        self.weight = 1
        self.children = []
        self.parent = None


class Tree:
    def __init__(self, start_node: str):
        self.root = Node(start_node)

    # BFS iteration
    def __iter__(self):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            yield node
            nodes.extend(node.children)

    def add_node(self, data: str, parent: Node):
        node = Node(data)
        node.parent = parent
        parent.children.append(node)

    def get_chain(self, node: Node) -> list[str]:
        chain = []
        while node.parent:
            chain.append(node.data)
            node = node.parent

        chain.append(node.data) # root node

        return chain[::-1]


#
def ex8 () -> str:
    """

    Ex8: Let user type 2 words in English as input. Print out the output
    which is the shortest chain according to the following rules:
    - Each word in the chain has at least 3 letters
    - The 2 input words from user will be used as the first and the last words of the chain
    - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
    - All the words are from the file wordsEn.txt
    - If there are multiple shortest chains, return any of them is sufficient
    """
    start = input("please select the FIRST word of the chain: ")
    while len(start) < 3:
        start = input("please input a word longer than 3 characters")

    end = input("please select the LAST word of the chain: ")
    while len(end) < 3:
        end = input("please input a word longer than 3 characters")

    if start[-2:] == end[:2]:
        return f"{start} {end}"

    tree = Tree(start)

    with open("../wordsEn.txt") as f:
        words = [word.strip() for word in f.readlines()]

    for node in tree:
        for word in words:
            if len(word) < 3:
                continue

            w_beg = word[:2]
            w_end = word[-2:]

            if w_beg == node.w_end:
                if w_end == end[:2]:
                    chain = tree.get_chain(node)
                    chain.append(word)
                    chain.append(end)
                    return ' '.join(chain)
                tree.add_node(word, node)

    return "No chain could be made with the given words"


def main():
    while True:
        user_in = input().lower()

        if user_in == "exit":
            print("Goodbye\n")
            return

        if user_in == "run ex1": print(ex1())
        if user_in == "run ex2": print(ex2())
        if user_in == "run ex3": print(ex3())
        if user_in == "run ex4": print(ex4())
        if user_in == "run ex5": print(ex5())
        if user_in == "run ex6": print(ex6())
        if user_in == "run ex7": print(ex7())
        if user_in == "run ex8": print(ex8())

        print("\n")


if __name__ == "__main__":
    main()
