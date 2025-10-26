# Import necessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(50, 50, 250, 500)
        self.setWindowTitle("2.1 - Just a cute kitty")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create the labels to be displayed in the window."""
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Michelle")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(85, 230)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 260)

        about_label = QLabel(self)
        about_label.setText("I'm still a little fluffy kitten " \
        "who wants to become a big cat. I have a lot of " \
        "experience playing with balls and tыgыdыk.")
        about_label.setWordWrap(True)
        about_label.move(15, 290)

        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont('Arial', 17))
        skills_label.move(15, 350)

        languages_label = QLabel(self)
        languages_label.setText("I touch everyone around me." \
        "I can scream Meow for a long time, "
        "especially at night.")
        languages_label.move(15, 375)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 400)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Sofa Ripper")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 430)

        driver_label = QLabel(self)
        driver_label.setText("The flower eater")
        driver_label.move(15, 450)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("A broken vase and your heart")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 470)

    def createImageLabels(self):
        """Open image files and create image labels."""
        images = ["images/skyblue.png", 
                  "images/Kotik.png"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/Kotik.png":
                        label.move(25, 20) 
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")            

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
