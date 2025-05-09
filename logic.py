from PyQt6.QtWidgets import *
from voteSafe1 import *
import csv
import os


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Method to organize VoteSafe GUI and connect the buttons to our code
        """
        super().__init__()
        self.setupUi(self)

        self.btnSubmitVote.clicked.connect(self.submit_vote)


    def submit_vote(self) -> None:
        """
        Method to submit vote
        """

        age = self.inputAge.text().strip()

        voterID = self.inputVoterIDNumb.text().strip()
        status = "No"

        found = False

        try:
            age = int(age)
            if age < 18:
                self.labelMessage.setText("Must be 18 years of age or older to vote")
                return
        except ValueError:
            self.labelMessage.setText("Enter age, numbers only")
            return



        if voterID == '':
            self.labelMessage.setText("VoterID cannot be empty")
            return


        try:
            header = not os.path.isfile("dataVoteSafe.csv") or os.path.getsize("dataVoteSafe.csv") == 0
            with open('dataVoteSafe.csv', 'a+', newline='') as file:
                file.seek(0)
                reader = csv.DictReader(file)
                writer = csv.writer(file)
                if header:
                    writer.writerow(["VoterID", " Age", " Candidate"])

                for row in reader:
                    rowValue = row['VoterID']
                    if rowValue == voterID:
                        self.labelMessage.setText(f"VoterID {voterID} has already voted")
                        found = True
                        break
        except (KeyError):
            self.labelMessage.setText("VoterID not in system")

        if not found:
            status = "Yes"

        vote = ''

        if self.radioBtnCand1.isChecked() and age >= 18 and status == "Yes":
            vote = "John"
        elif self.radioBtnCand2.isChecked() and age >= 18 and status == "Yes":
            vote = "Jane"
        elif self.radioBtnWI.isChecked() and age >= 18 and status == "Yes":
            vote = self.inputWI.text().strip()

        header = not os.path.isfile("dataVoteSafe.csv") or os.path.getsize("dataVoteSafe.csv") == 0


        if len(vote) > 0:
            self.labelMessage.setText(f"Thank you for voting")
            with open("dataVoteSafe.csv", "a", newline='') as file:
                writer = csv.writer(file)
                if header:
                    writer.writerow(["VoterID", "Age", "Candidate"])
                writer.writerow([voterID,age,vote])

                self.inputWI.clear()
                self.inputAge.clear()
                self.inputVoterIDNumb.clear()

                self.radioBtnWI.setAutoExclusive(False)
                self.radioBtnWI.setChecked(False)
                self.radioBtnWI.setAutoExclusive(True)

                self.radioBtnCand1.setAutoExclusive(False)
                self.radioBtnCand1.setChecked(False)
                self.radioBtnCand1.setAutoExclusive(True)

                self.radioBtnCand2.setAutoExclusive(False)
                self.radioBtnCand2.setChecked(False)
                self.radioBtnCand2.setAutoExclusive(True)







