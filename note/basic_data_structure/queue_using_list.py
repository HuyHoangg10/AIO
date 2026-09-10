# ==============================================================================
# QUEUE DATA STRUCTURE: FIFO (First In First Out)
# Thằng nào vào đầu tiên sẽ bị bốc ra đầu tiên.
# ==============================================================================
class Queue:
    def __init__(self, capacity):
        self.__data = []          # Private property để bảo vệ dữ liệu nội bộ
        self.capacity = capacity  # Sức chứa tối đa của hàng đợi

    def describe(self):
        print(self.__data)

    # Thêm phần tử vào CUỐI hàng đợi (Xếp hàng vào sau)
    def add(self, item):
        if len(self.__data) < self.capacity:
            self.__data.append(item)
        else:
            print("⚠️ Queue Overflow: Hàng đợi đã đầy!")

    # Lấy phần tử ở ĐẦU hàng đợi ra (Thằng đến trước được đi ra trước)
    def remove(self):
        if len(self.__data) > 0:
            # Dùng pop(0) để bốc thằng ở vị trí index 0 (đầu mảng) ra ngoài
            return self.__data.pop(0)
        else:
            print("⚠️ Queue Underflow: Hàng đợi trống rỗng!")
            return None


# ==============================================================================
# EXECUTION (Chạy thử nghiệm hệ thống để thấy sự khác biệt với Stack)
# ==============================================================================
queue = Queue(5)
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)

print("Queue before remove:")
queue.describe()  # Result: [10, 20, 30, 40]

print("\nQueue after remove (First In First Out):")
# Thằng 10 vào đầu tiên, nên khi remove, thằng 10 phải biến mất đầu tiên!
queue.remove()    
queue.describe()  # Result: [20, 30, 40]