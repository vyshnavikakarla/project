
from flask import Flask,jsonify,request
app=Flask(__name__)
doctors=[
    {
        "id":1,
        "name":"Dr.Smith",
        "speciality":"cardiologist",
        "schedule":{
            "Monday":"5:00 PM - 8:00 PM",
            "Tuesday":"5:00 PM - 8:00 PM",
            "Wednesday":"5:00 PM - 8:00 PM",
            "Thursday":"5:00 PM - 8:00 PM",
            "Friday":"5:00 PM - 8:00 PM",
            "Saturday":"5:00 PM - 8:00 PM",
            "Sunnday":"Day off"
        },
        "max_patients":10
    }
]
appointments=[]
def get_doctors():
    return jsonify(doctors)
def get_doctor(doctor_id):
    doctor=next((doctor for doctor in doctors if doctor['id']==doctor_id),None)
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error":"Doctor not found"}),404
def get_availability(doctor_id):
    doctor=next((doctor for doctor in doctors if doctor['id']==doctor_id),None)
    if doctor:
        availability={"Monday":["5:00 PM","6:00 PM","7:00 PM"]}
        return jsonify(availability)
    else:
        return jsonify({"error":"Doctor not found"}),404
def book_appointment():
    data=request.json
    appointments.append(data)
    return jsonify({"message":"Appointment booked successfully"})

if __name__=='__main__':
    #from waitress import serve
    #serve(app,host="0.0.0.0",port=5000,threads=2)
    app.run(debug = True)
