from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys
from passenger import Passenger
from flight import Flight, Local_Flight
from airline import Airline
from International_flight import International_flight, I_flight

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Flight Management System")

    airline = Airline("AB Airways")
    domestic = Local_Flight("AB123", "Tokyo", "Sapporo", 10)
    international = I_flight("AB156", "Hong Kong", "Tokyo", 10)

    flights = [domestic, international]
    for f in flights:
        airline.add_flight(f)

    flight_numbers = [f.get_flight_number() for f in airline.get_flight()]
    label = QLabel("Flights:\n" + "\n".join(flight_numbers))

    name_input = QLineEdit()
    name_input.setPlaceholderText("Passenger name")

    passport_input = QLineEdit()
    passport_input.setPlaceholderText("Passport number")

    age_input = QLineEdit()
    age_input.setPlaceholderText("Age")

    gender_input = QLineEdit()
    gender_input.setPlaceholderText("Gender (M/F)")

    def add_passenger():
        name = name_input.text()
        passport = passport_input.text()
        age_text = age_input.text()
        gender = gender_input.text()

        if not name or not passport or not gender or not age_text:
            label.setText("Please fill in all fields.")
            return

        try:
            age = int(age_text)
        except ValueError:
            label.setText("Age must be a number.")
            return

        p = Passenger(name, passport, age, gender)
        
        p.set_name(name)
        p.set_passport_number(passport)
        p.set_age(age_text)
        p.set_sex(gender)
        domestic.add_passenger(p)

        lines = [airline.display_airline()]
        for f in airline.get_flight():
            lines.append(f.display_flight())
            for passenger in f.get_passengers():
                lines.append(passenger.display_passenger())

        text = "\n".join(lines)
        label.setText(text)

        name_input.clear()
        passport_input.clear()
        age_input.clear()
        gender_input.clear()

    button = QPushButton("Add Passenger")
    button.clicked.connect(add_passenger)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name_input)
    layout.addWidget(passport_input)
    layout.addWidget(age_input)
    layout.addWidget(gender_input)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
