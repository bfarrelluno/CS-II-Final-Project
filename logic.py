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

        self.vote_1 = 0
        self.vote_2 = 0
        self.vote_3 = 0
        self.vote_total = 0

        self.voteButton.clicked.connect(lambda: self.vote_menu())
        self.exitButton.clicked.connect(lambda: self.log_votes())

    def vote_menu(self) -> None:
        """
        Function that logs what candidate is selected when the
        Vote button is hit.  It also adds to the respective candidate's
        counter and the total vote count.
        :param self: Parameter that refers to itself.
        """
        if self.radioButton1.isChecked():
            self.vote_1 += 1
            self.vote_total += 1
            self.outputLabel.setText(f'Voted Cameron\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')
        if self.radioButton2.isChecked():
            self.vote_2 += 1
            self.vote_total += 1
            self.outputLabel.setText(f'Voted Allison\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')
        if self.radioButton3.isChecked():
            self.vote_3 += 1
            self.vote_total += 1
            self.outputLabel.setText(f'Voted Diego\nCameron - {self.vote_1}\nAllison - {self.vote_2}\nDiego - {self.vote_3}\nTotal - {self.vote_total}')

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

