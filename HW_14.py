"""
כתוב מחלקה בשם Shape המכילה שם של צורה. קבל את שם הצורה כפרמטר בפונקציה __init .__
כתוב __str __המדפיס את שם הצורה.
כתוב מחלקה היורשת ממחלקת Shape בשם FourSides המייצגת מרובע, ומקבלת ב __init __את
אורך ארבעת הצלעות שלו )לדוגמא ע"י פרמטרים בשם d, c, b, a + שם הצורה(. קרא ל __init__
של מחלקת האבא. כתוב __str __המדפיס את אורך כל הצלעות וקורא ל __str __של מחלקת
האבא. הוסף פונקציה בשם getHekef אשר מחזירה את היקף המרובע. הוסף את היקף המרובע ל
__str__
*אתגר: כתוב מחלקה בשם Rectangle( מלבן( היורשת ממחלקת FourSides ומקבלת ב __init__
את אורך ורוחב המלבן )שני פרמטרים + שם הצורה(. כתוב __str __מתאים. הוסף פונקציה בשם
getArea המחשבת את שטח המלבן. הוסף את שטח המלבן ל __str__
* אתגר: כתוב מחלקה בשם Square( ריבוע( היורשת ממחלקת Rectangle ומקבלת ב __init __את
גודל צלע הריבוע )פרמטר אחד + שם הצורה(. כתוב __str __מתאים. בצע override לפונקצית
חישוב ההיקף וחישוב השטח
"""


class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def __str__(self):
        return f'{self.shape_name} - Shape'


class FourSided(Shape):
    def __init__(self, s_name, a, b, c, d):
        super().__init__(s_name)
        self.sides = [a, b, c, d]

    def circumference(self):
        return sum(self.sides)

    def __str__(self):
        return super().__str__() + \
               f'\nside a: {self.sides[0]}\n' \
               f'side b: {self.sides[1]}\n' \
               f'side c: {self.sides[2]}\n' \
               f'side d: {self.sides[3]}\n' \
               f'circumference is {self.circumference()}\n'


class Rectangle(FourSided):
    def __init__(self, s_name, sides_a, sides_b):
        super().__init__(s_name, sides_a, sides_b, sides_a, sides_b)

    def area(self):
        return self.sides[0] * self.sides[1]
    def __str__(self):
        return f'Rectangle - \'{self.shape_name}\'\n' \
            f'area: {self.area()}\n' \
            f'Circumference: {self.circumference()}'

class Square(Rectangle):
    def __init__(self, s_name, sides):
        super().__init__(s_name, sides, sides)

    def __str__(self):
        return f'Square - \'{self.shape_name}\'\n' \
            f'area: {self.area()}\n' \
            f'Circumference: {self.circumference()}'


b = Square('box', 5)

print(b)
