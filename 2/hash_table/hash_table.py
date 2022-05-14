class HashTable:
    '''
    m:
        rozmiar tablicy m

    type: 
        1 – metoda łańcuchowa 
        2 – adresowanie liniowe 
        3 – adresowanie kwadratowe 
        4 – haszowanie dwukrotne

    h1: 
        funkcja haszująca
    h2:
        druga funkcja haszująca w przypadku haszowania dwukrotnego 
    '''

    def __init__(self, size, type):
        self.m = size
        self.type = type
        self.array = size * [None]

    def insert(self, element):
        option = self.type
        if option == 1:
            index = self.h(element)
            if self.array[index] is None: # no element
                self.array[index] = element
            elif isinstance(self.array[index], list): # two or more elements
                self.array[index].insert(0, element)
            else: # just one element
                temp = self.array[index]
                self.array[index] = []
                self.array[index].insert(0, temp)
                self.array[index].insert(0, element)
        else:
            i = 0
            while i != self.size():
                j = self.h(element, i)
                if self.array[j] is None:
                    self.array[j] = element
                    return
                else:
                    i += 1

    def delete(self, element):
        option = self.type
        if option == 1:
            index = self.h(element)
            if isinstance(self.array[index], list): # two or more elements at the index
                self.array[index].remove(element) 
                if not self.array[index]: # if the sublist is empty
                    self.array[index] = None 
                elif len(self.array[index]) == 1: # if there is just one element
                    temp = self.array[index][0]
                    self.array[index] = temp
            else: # just one element
                self.array[index] = None # empty the place of the element in the list
        else:
            index = self.search(element)
            self.array[index] = 'Deleted'

    def search(self, element):
        option = self.type
        if option == 1:
            index = self.h(element)
            return index
        else:
            i = 0
            while True:
                j = self.h(element, i)
                if self.array[j] == element:
                    return j
                i += 1
                if i == self.size() or self.array[j] is None:
                    break

    def size(self):
        return self.m

    def h(self, key, i=None):
        option = self.type
        if option == 1:
            return self.h1(key)
        elif option == 2:
            return (self.h1(key) + i) % self.size()
        elif option == 3:
            return (self.h1(key) + i + i*i) % self.size()
        elif option == 4:
            return (self.h1(key) + i * self.h2(key)) % self.size()

    def h1(self, key):
        return key % self.size()

    def h2(self, key):
        return (key % (self.size() - 1)) + 1

    def print(self):
        print('[', end='')
        for element in self.array:
            if element == "Deleted":
                print("Deleted", end=', ')
            else:
                print(element, end=', ')
        print('\b\b]', end='\n')

def parse_input():
    try:
        text = input()
        return [int(str) for str in text.split()]
    except:
        return None

def main():
    data = parse_input()

    size = data[0]
    type = data[1]
    elements = data[2:]

    table = HashTable(size, type)

    for element in elements:
        table.insert(element)

    table.print()

    while True:
        data = parse_input()
        if not data:
            break

        option = data[0]
        if option == -1:
            break

        element = data[1]

        if option == 0:
            table.insert(element)
            table.print()
        elif option == 1:
            searched = table.search(element)
            print(searched)
        elif option == 2:
            table.delete(element)
            table.print()

if __name__ == '__main__':
    main()