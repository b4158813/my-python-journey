import sys
from PyQt5 import QtWidgets
from huire_cycle import Ui_ThermodynamicsAssignments
from CALCULATE_ALL import Solution


class MyPyQT_Form(QtWidgets.QWidget, Ui_ThermodynamicsAssignments):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 实现calculate_answer()函数，textEdit是我们放上去的文本框的id
    def calculate_answer(self):
        self.nt, self.d, self.nt_lang, self.d_lang, self.nt_real = solve_3()
        self.textBrowser.setText('ηt = '+self.nt+'\nd = '+self.d+'\nηt_lang = '+self.nt_lang+'\nd_lang = '+self.d_lang+'\nηt_real = '+self.nt_real)


def solve_3():
    solution3 = Solution()
    ans3 = solution3.calculate_3(3317.5, 2100, 152, 2748.6, 640)
    return ans3


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
