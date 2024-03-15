import datetime
import json

import requests

from pprint import pprint


def calculate_medical_score(health_record):
    # Initialize the score
    """
    The calculate_medical_score function takes a health record and returns an integer score.
    The score is calculated based on the following criteria:
        - 10 points for having blood pressure readings of 120/80 or higher
        - 5 points for being prescribed aspirin
        - 20 points per active problem in the patient's medical history (e.g., diabetes, heart disease)
        - 10 points if there are any progress notes indicating that blood pressure readings are stable

    :param health_record: Pass in the health record of a patient
    :return: The medical score for a patient
    :doc-author: Harbhajan Rai
    """
    score = 0

    # Calculate score based on blood pressure
    systolic = health_record["medicalRecord"]["systolicValue"]
    diastolic = health_record["medicalRecord"]["diastolicValue"]
    if systolic >= 120 and diastolic >= 80:
        score += 10

    # Calculate score based on prescriptions
    for prescription in health_record["prescriptions"]:
        if prescription["name"] == "Aspirin":
            score += 5

    # Calculate score based on problems
    for problem in health_record["problems"]:
        if problem["status"] == "active":
            score += 20
        for progress_note in problem.get("progressNotes", []):
            if "Blood pressure readings are stable." in progress_note.get("note", ""):
                score += 10

    return score


def process_heath_record():
    """
    The process_heath_record function takes a user's unique ID and returns the following information:
        - The user's name
        - The user's email address
        - The number of problems in their health record (e.g., diabetes, high blood pressure)
        - The number of prescriptions in their health record (e.g., insulin, metformin)


    :return: A dictionary with the following keys:
    :doc-author: Harbhajan Rai
    """
    url = "http://127.0.0.1:5000/api/health_record/123"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)

    heath_record = response.json()

    record = {
        'user_name': heath_record['user']['name'],
        'email': heath_record['user']['email'],
        'problemCount': len(heath_record['problems']),
        'prescriptionsCount': len(heath_record['prescriptions']),
        'device': heath_record['device']
    }
    medical_score = calculate_medical_score(
        heath_record
    )
    record['medical_score'] = medical_score

    return record


def update_health_record(id):
    """
    The update_health_record function takes in a patient ID and updates the health record of that patient.
        The function returns the updated health record.

    :param id: Specify which health record to update
    :return: The updated record
    :doc-author: Harbhajan Rai
    """
    new_records = {
        "type": "medicalRecord",
        "BloodPressure": {
            "type": "BloodPressure",
            "systolicValue": 130,
            "diastolicValue": 90,
            "recordTime": str(datetime.datetime.now())
        },
        "OxygenLevel": {
            "value": 94,
            "recordTime": str(datetime.datetime.now())
        }

    }
    url = "http://127.0.0.1:5000/health_record/123"

    payload = json.dumps(new_records)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.json()


def submit_prescriptions(patient_id):
    """
    The submit_prescriptions function takes in a patient_id and returns the updated prescription information for that patient.
    The function does this by making a PATCH request to the /patients/&lt;patient_id&gt;/prescriptions endpoint, passing in new prescription data as JSON.

    :param patient_id: Identify which patient's prescriptions are being updated
    :return: A dictionary with the updated prescriptions
    :doc-author: Harbhajan Rai
    """
    new_prescription = {
        "name": "Metformin",
        "dosage": "500mg",
        "frequency": "twice daily",
        "notes": "avoid curd"
    }

    url = f"http://127.0.0.1:5000/patients/{patient_id}/prescriptions"

    payload = json.dumps(new_prescription)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    return response.json()


def check_coverage(medical_score):
    """
    The check_coverage function checks if the medical score is above 50.
        If it is, then coverage will be approved. Otherwise, coverage will be denied.

    :param medical_score: Determine if the coverage is approved or denied
    :return: A tuple of two values
    :doc-author: Harbhajan Rai
    """
    coverage_threshold = 50  # Define the threshold score for coverage

    if medical_score >= coverage_threshold:
        return True, "Coverage approved."
    else:
        return False, "Coverage denied, medical score is below 50"


update_health_record(123456789)
submit_prescriptions(123456789)
processed_record = process_heath_record()
pprint(process_heath_record())

coverage_approved, message = check_coverage(processed_record['medical_score'])

print("Medical Score:", processed_record['medical_score'])
print(message)
