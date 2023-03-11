''' 
Реализовать класс и переопределить магические методы базовых математических операции 
(сложение, вычитание, умножение, деление), добавив туда выводы в консоль текущего действия.

Например: при умножении выводится сообщение, что происходит умножение.
'''

class NewMath(int):
    def __init__(self, num) -> int:
        super().__init__()
        self.num = num

    def __add__(self, num2):
        print(f'\nпроисходит вычетание из {self.num} вычетаем {num2}')
        return self.num - num2

    def __sub__(self, num2):
        print(f'\nпроисходит сложение  к {self.num} прибавляем {num2}')
        return self.num + num2

    def __mul__(self, num2):
            print(f'\nпроисходит деление  {self.num} на {num2}')
            return self.num / num2

    def __truediv__(self, num2):
        print(f'\nпроисходит умножение {self.num} на {num2}')
        return self.num * num2


MagicNum = NewMath(6)

print(MagicNum + 2 )
print(MagicNum - 2 )
print(MagicNum * 2 )
print(MagicNum / 2 )
