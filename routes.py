#!/usr/bin/python3
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify
from model import db


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///med.db'
db.init_app(app)

app = Flask(__name__)
users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

doctors =  {
    "Nafiu": 
    "Ahmed"
}
post {
    "id" = 1
    "id": 2
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    ''' Check if the user already exists in the database'''
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 409  # 409 Conflict

    ''' If the user doesn't exist, create a new user and add them to the database'''
    new_user = User(username=username, generate_password_hash(password))

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'Registration failed'}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    ''' Check if the user exists in the database'''
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401  # 401 Unauthorized


@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()
    time = data.get('time')
    date = data.get('date')
    username = data.get('username')

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'User not found'})
    appointment = Appointment(user_id=user.id, date=date, time=time)
    try:
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment successfully booked'}), 201
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'Booking appointment failed'}), 400


@app.route('/appointment/<int>: id', methods=['POST'])
def update_appointment(appointment_id)
    pass

@app.route('/appointment/<int>: id')
@app.route('/payment', methods=['POST', 'GET'])
def payment():
    if request.method == 'POST':
        return jsonify({'message': 'Payment processed successfully'}), 200
    else:
        return jsonify({'message': 'Please provide payment detail'}), 200


@app.route('/doctors', methods=['POST', 'GET'])
def get_doctors():
    doctors = Doctor.query.all()
    doctor_list = [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]
    return jsonify(doctor_list), 200

@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        return jsonify({'id': doctor.id, 'name': doctor.name, 'specialty': doctor.specialty}), 200
    return jsonify({'message': 'Doctor not found'}), 404


@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    name = data.get('name')
    specialty = data.get('specialty')
    email = data.get('email')
    license = data.get('license')
    
    new_doctor = Doctor(name=name, email=email, specialty=specialty, license=license)
    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({'message': 'Doctor successfully added'}), 200


@app.route('/doctors/<int:id>', methods=['PUT'])
def update_doctors(id):
    doctor = Doctor.query.get(id)
    if doctor:
        data = request.get_json()
        doctor.name = data.get('name', doctor.name)
        doctor.specialty = data.get('specialty', doctor.specialty)
        db.session.commit()
        return jsonify({'message': 'Doctor updated successfully'}), 200
    else:
        return jsonify({'message': 'Doctor not found'}), 404


@app.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({'message': 'Doctor removed successfully'}), 200
    else:
        return jsonify({'message': 'Doctor not found'}), 404


@app.route('/posts/<int:id>', methods=['POST'])
def create_posts():
    pass

@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(post.id):
    pass


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(post.id)
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
