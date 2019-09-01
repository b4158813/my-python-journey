import sys
from PyQt5 import QtWidgets
from langken_cycle_1 import Ui_ThermodynamicsAssignments
from CALCULATE_ALL import Solution


class MyPyQT_Form(QtWidgets.QWidget, Ui_ThermodynamicsAssignments):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 实现calculate_answer()函数，textEdit是我们放上去的文本框的id
    def calculate_answer(self):

        self.textBrowser.setText('ηt = '+solve_1()+'\n'+'ηt_real = '+str(0.85*eval(str(solve_1())[:-1]))+'%')


def solve_1():
    solution1 = Solution()
    ans1 = solution1.calculate_1(3331.2, 2136.8, 151.95)
    return ans1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
