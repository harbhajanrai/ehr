import json

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


false = False
true = True

patients_details = {}

patients = ["123456789"]

health_record = {
    "uuid": "E6F2FED4-6547-4DF8-A3F3-DC7E67C6D044",
    "startDate": "2022-01-01T08:00:00Z",
    "endDate": "2022-01-01T08:30:00Z",
    "type": "MindfulSession",
    "value": "MindfulSession",
    "source": {
        "name": "Headspace",
        "bundleIdentifier": "com.headspace.headspace"
    },
    "device": {
        "name": "Apple Watch",
        "manufacturer": "Apple",
        "model": "Series 6",
        "hardwareVersion": "1.0",
        "softwareVersion": "8.0"
    },
    "user": {
        "id": "123456789",
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    "medicalRecord": {
        "type": "BloodPressure",
        "systolicValue": 120,
        "diastolicValue": 80,
        "unit": "mmHg",
        "metadata": {
            "BloodPressureLocation": "Left Arm"
        }
    },
    "prescriptions": [
        {
            "name": "Aspirin",
            "dosage": "75mg",
            "frequency": "daily"
        }
    ],
    "problems": [
        {
            "name": "Hypertension",
            "status": "active",
            "onsetDate": "2021-01-01",
            "progressNotes": [
                {
                    "date": "2022-03-15",
                    "note": "Blood pressure readings are stable."
                }
            ]
        }
    ]
}

# Mock data
mock_data = {
    "resourceType": "Patient",
    "id": "12724067",
    "meta": {
        "versionId": "10",
        "lastUpdated": "2020-07-06T21:21:22.000Z"
    },
    "extension": [
        {
            "id": "59434424",
            "extension": [
                {
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4640016",
                                "code": "485602703",
                                "display": "Appointment Reminders",
                                "userSelected": true
                            },
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/communication-topic",
                                "code": "appointment-reminder",
                                "display": "Appointment Reminder",
                                "userSelected": false
                            }
                        ],
                        "text": "Appointment Reminders"
                    },
                    "url": "communication-type"
                },
                {
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/23042",
                                "code": "495085513",
                                "display": "Fax",
                                "userSelected": true
                            },
                            {
                                "system": "http://hl7.org/fhir/contact-point-system",
                                "code": "fax",
                                "display": "Fax",
                                "userSelected": false
                            }
                        ],
                        "text": "Fax"
                    },
                    "url": "contact-method"
                },
                {
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/43",
                                "code": "163",
                                "display": "Business",
                                "userSelected": true
                            },
                            {
                                "system": "http://hl7.org/fhir/contact-point-use",
                                "code": "work",
                                "display": "Work",
                                "userSelected": false
                            }
                        ],
                        "text": "Business"
                    },
                    "url": "contact-type"
                },
                {
                    "valueDateTime": "2019-04-13T20:00:00.000Z",
                    "url": "verified-datetime"
                }
            ],
            "url": "https://fhir-ehr.cerner.com/r4/StructureDefinition/communication-preference"
        },
        {
            "extension": [
                {
                    "valueCoding": {
                        "system": "urn:oid:2.16.840.1.113883.6.238",
                        "code": "2106-3",
                        "display": "White",
                        "userSelected": false
                    },
                    "url": "ombCategory"
                },
                {
                    "valueString": "White",
                    "url": "text"
                }
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
        },
        {
            "extension": [
                {
                    "valueCoding": {
                        "system": "urn:oid:2.16.840.1.113883.6.238",
                        "code": "2186-5",
                        "display": "Non Hispanic or Latino",
                        "userSelected": false
                    },
                    "url": "ombCategory"
                },
                {
                    "valueString": "Not Hispanic, Latino, or Spanish Origin",
                    "url": "text"
                }
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
        }
    ],
    "identifier": [
        {
            "id": "CI-490016886-0",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "10",
                        "display": "MRN",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "MR",
                        "display": "Medical record number",
                        "userSelected": false
                    }
                ],
                "text": "MRN"
            },
            "system": "urn:oid:2.16.840.1.113883.6.1000",
            "value": "6931",
            "period": {
                "start": "2019-12-26T15:14:12.000Z"
            }
        },
        {
            "id": "CI-490058771-1",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "10",
                        "display": "MRN",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "MR",
                        "display": "Medical record number",
                        "userSelected": false
                    }
                ],
                "text": "MRN"
            },
            "system": "urn:oid:2.16.840.1.113883.6.1000",
            "value": "6978",
            "period": {
                "end": "2020-07-06T21:21:25.000Z"
            }
        },
        {
            "id": "CI-490059574-3",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "670843",
                        "display": "Messaging",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "U",
                        "display": "Unspecified identifier",
                        "userSelected": false
                    }
                ],
                "text": "Messaging"
            },
            "_system": {
                "extension": [
                    {
                        "valueCode": "unknown",
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
                    }
                ]
            },
            "value": "3C36293A3B964994AD8E6C0305F3330A",
            "period": {
                "start": "2020-06-30T20:08:26.000Z"
            }
        },
        {
            "id": "CI-490058805-4",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "670843",
                        "display": "Messaging",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "U",
                        "display": "Unspecified identifier",
                        "userSelected": false
                    }
                ],
                "text": "Messaging"
            },
            "_system": {
                "extension": [
                    {
                        "valueCode": "unknown",
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
                    }
                ]
            },
            "value": "43DA797A657B47548F258A9B50EB41F5",
            "period": {
                "start": "2020-06-12T16:03:32.000Z"
            }
        },
        {
            "id": "CI-490059570-5",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "2553236771",
                        "display": "Federated Person Principal",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "AN",
                        "display": "Account number",
                        "userSelected": false
                    }
                ],
                "text": "Federated Person Principal"
            },
            "system": "urn:oid:2.16.840.1.113883.3.13.6",
            "value": "URN:CERNER:IDENTITY-FEDERATION:REALM:E8A84236-C258-4952-98B7-A6FF8A9C587A-CH:PRINCIPAL:AN7TD9A62CV8Z53Z",
            "period": {
                "start": "2020-06-30T20:08:25.000Z"
            }
        },
        {
            "id": "CI-490058801-6",
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4",
                        "code": "2553236771",
                        "display": "Federated Person Principal",
                        "userSelected": true
                    },
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "AN",
                        "display": "Account number",
                        "userSelected": false
                    }
                ],
                "text": "Federated Person Principal"
            },
            "system": "urn:oid:2.16.840.1.113883.3.13.6",
            "value": "URN:CERNER:IDENTITY-FEDERATION:REALM:E8A84236-C258-4952-98B7-A6FF8A9C587A-CH:PRINCIPAL:KR8KC9MI9EQ8KC23",
            "period": {
                "start": "2020-06-12T16:03:29.000Z"
            }
        }
    ],
    "active": true,
    "name": [
        {
            "id": "CI-12724067-0",
            "use": "official",
            "text": "SMART, JOE",
            "family": "SMART",
            "given": [
                "JOE"
            ],
            "period": {
                "start": "2019-12-26T15:14:12.000Z"
            }
        },
        {
            "id": "CI-490059796-0",
            "use": "old",
            "text": "SMART, STEPHEN ALLEN",
            "family": "SMART",
            "given": [
                "STEPHEN",
                "ALLEN"
            ],
            "period": {
                "end": "2020-07-06T21:21:26.000Z"
            }
        }
    ],
    "telecom": [
        {
            "id": "CI-PH-29811920-0",
            "extension": [
                {
                    "valueUrl": "(816)888-8886",
                    "url": "http://hl7.org/fhir/StructureDefinition/iso21090-TEL-address"
                },
                {
                    "valueString": "12345",
                    "url": "http://hl7.org/fhir/StructureDefinition/contactpoint-extension"
                }
            ],
            "system": "phone",
            "value": "8168888886",
            "use": "home",
            "rank": "1",
            "period": {
                "start": "2019-12-26T15:14:12.000Z"
            }
        },
        {
            "id": "CI-EM-29822662-0",
            "system": "email",
            "value": "joesmart@yopmail.com",
            "use": "home",
            "rank": "1",
            "period": {
                "start": "2020-03-30T19:31:11.000Z"
            }
        }
    ],
    "gender": "male",
    "birthDate": "1976-04-29",
    "deceasedBoolean": false,
    "address": [
        {
            "id": "CI-24313553-0",
            "use": "home",
            "text": "12345 Main St\\nKansas city, MO 64116\\nUS",
            "line": [
                "12345 Main St"
            ],
            "city": "Kansas city",
            "district": "Jackson",
            "state": "MO",
            "postalCode": "64116",
            "country": "US",
            "period": {
                "start": "2019-12-26T15:13:36.000Z"
            }
        }
    ],
    "maritalStatus": {
        "coding": [
            {
                "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/38",
                "code": "309237",
                "display": "Married",
                "userSelected": true
            },
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                "code": "M",
                "display": "Married",
                "userSelected": False
            }
        ],
        "text": "Married"
    },
    "communication": [
        {
            "language": {
                "coding": [
                    {
                        "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/36",
                        "code": "151",
                        "display": "English",
                        "userSelected": True
                    },
                    {
                        "system": "urn:ietf:bcp:47",
                        "code": "en",
                        "display": "English",
                        "userSelected": False
                    }
                ],
                "text": "English"
            },
            "preferred": True
        }
    ],
    "generalPractitioner": [
        {
            "id": "CI-490017023-0",
            "reference": "Practitioner/4122622",
            "display": "Cerner Test, Physician - Hospitalist Cerner"
        }
    ]
}


@app.route("/api/patient", methods=["POST"])
def create_patient():
    """
    The create_patient function creates a new patient and returns the id of the newly created patient.

    :return: A tuple that contains a json object and the http status code 201
    :doc-author: Harbhajan Rai
    """
    patient_id = len(patients) + 1
    patient = {"id": str(patient_id)}
    patients.append(patient)
    return jsonify({"id": str(patient_id)}), 201


@app.route("/api/patient/<patient_id>")
def get_patient(patient_id):
    """
    The get_patient function returns a JSON object containing the patient's information.


    :param patient_id: Identify the patient
    :return: A json object
    :doc-author: Harbhajan Rai
    """
    return jsonify(mock_data)


@app.route("/api/patient", methods=["GET"])
def search_patient():
    # Extract query parameters from the request
    """
  The search_patient function is a mock endpoint that returns a list of patients matching the search criteria.
      ---
      tags:
        - Patient Search API

  :return: A list of patients
  :doc-author: Harbhajan Rai
  """
    parameters = request.args.to_dict()

    # Mock response data
    response_data = {
        "resourceType": "Bundle",
        "id": "b8e08a98-849f-4544-9fa8-985aa445e31b",
        "type": "searchset",
        "total": 2,
        "entry": [
            {
                "id": "CI-12724067-0",
                "use": "official",
                "text": "SMART, JOE",
                "family": "SMART",
                "given": [
                    "JOE"
                ],
                "period": {
                    "start": "2019-12-26T15:14:12.000Z"
                }
            },
            {
                "id": "CI-490059796-0",
                "use": "old",
                "text": "SMART, STEPHEN ALLEN",
                "family": "SMART",
                "given": [
                    "STEPHEN",
                    "ALLEN"
                ],
                "period": {
                    "end": "2020-07-06T21:21:26.000Z"
                }
            }
        ]
    }

    return jsonify(response_data)


@app.route("/api/health_record/<id>")
def get_patient_health_records(id):
    """
    The get_patient_health_records function returns the health records of a patient with the given id.


    :param id: Identify the patient
    :return: A json object containing the patient's health records
    :doc-author: Harbhajan rai
    """
    return jsonify(health_record)


@app.route("/health_record/<id>", methods=["PUT"])
def update_patient_record(id):
    """
    The update_patient_record function updates the patient's medical record.
        It takes in a patient id and returns a message that the update was successful.

    :param id: Specify the patient whose record is to be updated
    :return: A json response with the message “patient record updated successfully” and a status code of 200
    :doc-author: Harbhajan Rai
    """
    if id not in patients:
        return jsonify({"error": "Patient not found"}), 404
    update_data = request.json
    health_record['medicalRecord'].update(update_data)

    return jsonify({"message": "Patient record updated successfully"}), 200
    # return jsonify(health_record)


@app.route("/patients/<patient_id>/prescriptions", methods=["PATCH"])
def submit_prescription(patient_id):
    """
    The submit_prescription function takes in a patient_id and adds the prescription to the health record.
        It returns a message indicating that the prescription was submitted successfully.

    :param patient_id: Identify the patient that is submitting the prescription
    :return: A json object and a status code
    :doc-author: Harbhajan Rai
    """
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404

    new_prescription = request.json
    health_record["prescriptions"].append(new_prescription)

    # return jsonify({"message": "Prescription submitted successfully"}), 200
    return jsonify(health_record)


if __name__ == "__main__":
    app.run(debug=True)
