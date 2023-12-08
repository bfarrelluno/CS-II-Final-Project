from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Function that initializes the Logic class
        Ensures the Vote and Exit buttons work when pressed
        Additionally, it sets up the numbers for the vote menu
        :param self: Parameter that refers to itself.
        """
        super().__init__()
        self.setupUi(self)
        self.voteButton1.hide()
        self.voteButton2.hide()
        self.voteButton3.hide()

        self.vote_1 = 0
        self.vote_2 = 0
        self.vote_3 = 0
        self.vote_total = 0

        self.voteButton.clicked.connect(lambda: self.vote_menu())
        self.voteButton1.clicked.connect(lambda: self.vote_func_1())
        self.voteButton2.clicked.connect(lambda: self.vote_func_2())
        self.voteButton3.clicked.connect(lambda: self.vote_func_3())
        self.exitButton.clicked.connect(lambda: self.log_votes())

    def vote_menu(self) -> None:
        """
        Function that switches the vote menu to the candidate menu,
        displaying the candidates for the candidate menu.
        :param self: Parameter that refers to itself.
        """
        self.voteButton.hide()
        self.exitButton.hide()
        self.voteButton1.show()
        self.voteButton2.show()
        self.voteButton3.show()
        self.mainLabel.setText("---------------\nCANDIDATE MENU\n---------------")

    def vote_func_1(self) -> None:
        """
        Function that logs candidate 1 when their respective
        radio button is checked.  It also adds to the respective candidate's
        counter and the total vote count before resetting back to the vote menu.
        :param self: Parameter that refers to itself.
        """
        self.vote_1 += 1
        self.vote_total += 1
        self.outputLabel.setText(f'Voted Cameron\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')
        self.voteButton1.hide()
        self.voteButton2.hide()
        self.voteButton3.hide()
        self.mainLabel.setText("---------------\nVOTE MENU\n---------------")
        self.voteButton.show()
        self.exitButton.show()

    def vote_func_2(self) -> None:
        """
        Function that logs candidate 2 when their respective
        radio button is checked.  It also adds to the respective candidate's
        counter and the total vote count before resetting back to the vote menu.
        :param self: Parameter that refers to itself.
        """
        self.vote_2 += 1
        self.vote_total += 1
        self.outputLabel.setText(f'Voted Allison\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')
        self.voteButton1.hide()
        self.voteButton2.hide()
        self.voteButton3.hide()
        self.mainLabel.setText("---------------\nVOTE MENU\n---------------")
        self.voteButton.show()
        self.exitButton.show()

    def vote_func_3(self) -> None:
        """
        Function that logs candidate 3 when their respective
        radio button is checked.  It also adds to the respective candidate's
        counter and the total vote count before resetting back to the vote menu.
        :param self: Parameter that refers to itself.
        """
        self.vote_3 += 1
        self.vote_total += 1
        self.outputLabel.setText(f'Voted Diego\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')
        self.voteButton1.hide()
        self.voteButton2.hide()
        self.voteButton3.hide()
        self.mainLabel.setText("---------------\nVOTE MENU\n---------------")
        self.voteButton.show()
        self.exitButton.show()

    def log_votes(self) -> None:
        """
        This function not only exits the program, but logs the
        current votes of each candidate as well as the total votes
        within a CSV file.
        :param self: Parameter that refers to itself.
        """
        votes = [f'Cameron - {self.vote_1}', f'Allison - {self.vote_2}', f'Diego - {self.vote_3}', f'Total - {self.vote_total}' ]
        with open('votes.csv', 'a') as f:
            data = csv.writer(f)
            data.writerow([votes])
        f.close()
        exit()

