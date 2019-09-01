import sys
from PyQt5 import QtWidgets
from zaire_cycle import Ui_ThermodynamicsAssignments
from CALCULATE_ALL import Solution


class MyPyQT_Form(QtWidgets.QWidget, Ui_ThermodynamicsAssignments):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 实现calculate_answer()函数，textEdit是我们放上去的文本框的id
    def calculate_answer(self):
        self.nt_lang_a1, self.nt_a1, self.x2_a1, self.nt_real_a1 = solve_2_1()
        self.nt_lang_a2, self.nt_a2, self.x2_a2, self.nt_real_a2 = solve_2_2()
        self.textBrowser.setText('ηt_lang_a1 = ' + self.nt_lang_a1 + '\nηt_a1 = ' + self.nt_a1 + '\nX2_a1 = ' + str(
            self.x2_a1) + '\nηt_a1_real = ' + self.nt_real_a1 + '\n\nηt_lang_a2 = ' + self.nt_lang_a2 + '\nηt_a2 = ' + self.nt_a2 + '\nX2_a2 = ' + str(
            self.x2_a2) + '\nηt_a2_real = ' + self.nt_real_a2)
        # self.textBrowser.setText('ηt = ' + self.nt)
        # self.textBrowser.setText('X2 = ' + str(self.x2))
        # self.textBrowser.setText('ηt_real = ' + self.nt_real)

    def summarize(self):
        self.summarize = '再热压力较高时，有利于提高ηt；再热压力较低时，有利于提高干度。'
        self.textBrowser_2.setText(self.summarize)


def solve_2_1():
    solution2 = Solution()
    nt_lang, nt, x2, nt_real = solution2.calculate_2(3349.6, 2183.6, 151.95, 3344.6, 2965.5, 2566.2, 1998.0)
    return nt_lang, nt, x2, nt_real


def solve_2_2():
    solution2 = Solution()
    nt_lang, nt, x2, nt_real = solution2.calculate_2(3349.6, 2421.7, 151.95, 3376.0, 2639.9, 2566.2, 1998.0)
    return nt_lang, nt, x2, nt_real


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
