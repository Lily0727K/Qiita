class Sample:
    def __init__(self):
        self.c_list = []

    def add_c_list(self, data):
        self.c_list.append(data)


sample1 = Sample()
sample1.add_c_list("data1")

sample2 = Sample()
sample2.add_c_list("data2")

print("sample1:", end=" ")
for item_data in sample1.c_list:
    print(item_data, end=" ")

print("sample2:", end=" ")
for item_data in sample2.c_list:
    print(item_data, end=" ")
