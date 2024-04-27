from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for doctors
doctors = [
    {
        "id": 1,
        "name": "Dr. Smith",
        "specialty": "Cardiologist",
        "schedule": {
            "Monday": "5:00 PM - 8:00 PM",
            "Tuesday": "5:00 PM - 8:00 PM",
            "Wednesday": "5:00 PM - 8:00 PM",
            "Thursday": "5:00 PM - 8:00 PM",
            "Friday": "5:00 PM - 8:00 PM",
            "Saturday": "5:00 PM - 8:00 PM",
            "Sunday": "Day off"
        },
        "max_patients": 10
    }
]

# Dummy data for appointments
appointments = []

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)

@app.route('/api/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((doctor for doctor in doctors if doctor['id'] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404

@app.route('/api/availability/<int:doctor_id>', methods=['GET'])
def get_availability(doctor_id):
    doctor = next((doctor for doctor in doctors if doctor['id'] == doctor_id), None)
    if doctor:
        # Dummy logic to calculate availability (e.g., based on current date and schedule)
        # You may need to implement a more sophisticated logic here
        availability = {"Monday": ["5:00 PM", "6:00 PM", "7:00 PM"]}
        return jsonify(availability)
    else:
        return jsonify({"error": "Doctor not found"}), 404

@app.route('/api/appointments/book', methods=['POST'])
def book_appointment():
    data = request.json
    # Dummy logic to book appointment
    appointments.append(data)
    return jsonify({"message": "Appointment booked successfully"})

if __name__ == '__main__':
    #from waitress import serve
    #serve(app,host="127.0.0.1",port=5000,threads=2)
    app.run(debug=True)
