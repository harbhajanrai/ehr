import requests


def get_patient(patient_id):

    """
    The get_patient function takes in a patient_id and returns the patient's information.
        Args:
            patient_id (int): The id of the desired patient

    :param patient_id: Get the patient's information from the database (right now getting mock data)
    :return: A dictionary with the patient's information
    :doc-author: Harbhajan rai
    """
    url = f"http://127.0.0.1:5000/api/patient/{patient_id}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to Fetch Response"


def search_patient(search_text):
    """
    The search_patient function takes in a search_text parameter and
     - returns the patient records that matches the search text.

    :param search_text: Search for a patient in the database
    :return: A list of patients that match the search text
    :doc-author: Trelent
    """
    url = f"http://127.0.0.1:5000/api/patient?search={search_text}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        search_response = response.json()
        return search_response['entry']
    else:
        return "No record found"


def create_new_patient():
    """
    The create_new_patient function creates a new patient in the FHIR server.
        The function takes no arguments and returns success code.


    :return: Return patient id
    :doc-author: Harbhajan Rai
    """
    url = "http://127.0.0.1:5000/api/patient"

    payload = {
        "resourceType": "Patient",
        "extension": [
            {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                "valueCode": "M"
            },
            {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                "extension": [
                    {
                        "url": "ombCategory",
                        "valueCoding": {
                            "system": "urn:oid:2.16.840.1.113883.6.238",
                            "code": "2028-9",
                            "display": "Asian"
                        }
                    },
                    {
                        "url": "detailed",
                        "valueCoding": {
                            "system": "urn:oid:2.16.840.1.113883.6.238",
                            "code": "2039-6",
                            "display": "Japanese"
                        }
                    }
                ]
            },
            {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                "extension": [
                    {
                        "url": "ombCategory",
                        "valueCoding": {
                            "system": "urn:oid:2.16.840.1.113883.6.238",
                            "code": "2186-5",
                            "display": "Non Hispanic or Latino"
                        }
                    }
                ]
            },
            {
                "url": "https://fhir-ehr.cerner.com/r4/StructureDefinition/communication-preference",
                "extension": [
                    {
                        "extension": [
                            {
                                "valueCodeableConcept": {
                                    "coding": [
                                        {
                                            "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/4640016",
                                            "code": "485602703",
                                            "display": "Appointment Reminder",
                                            "userSelected": False
                                        }
                                    ],
                                    "text": "Appointment Reminder"
                                },
                                "url": "communication-type"
                            },
                            {
                                "valueCodeableConcept": {
                                    "coding": [
                                        {
                                            "system": "https://fhir.cerner.com/ec2458f2-1e24-41c8-b71b-0e701af7583d/codeSet/23042",
                                            "code": "4054467",
                                            "display": "Phone",
                                            "userSelected": False
                                        }
                                    ]
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
                                            "userSelected": False
                                        }
                                    ],
                                    "text": "Home"
                                },
                                "url": "contact-type"
                            }
                        ],
                        "verified": "2019-12-26T15:41:52.000Z"
                    }
                ]
            }
        ],
        "identifier": [
            {
                "assigner": {
                    "reference": "Organization/675844"
                }
            }
        ],
        "active": True,
        "name": [
            {
                "use": "official",
                "family": "Wolf",
                "given": [
                    "Person",
                    "Name"
                ],
                "period": {
                    "start": "2010-05-17T14:54:31.000Z"
                }
            },
            {
                "use": "usual",
                "given": [
                    "Bigby"
                ],
                "period": {
                    "start": "2012-05-22T15:45:50.000Z"
                }
            }
        ],
        "telecom": [
            {
                "system": "phone",
                "value": "8168229121",
                "use": "home",
                "id": "CI-PH-29811920-0",
                "extension": [
                    {
                        "valueString": "12345",
                        "url": "http://hl7.org/fhir/StructureDefinition/contactpoint-extension"
                    }
                ],
                "period": {
                    "start": "2012-05-17T15:33:18.000Z"
                }
            }
        ],
        "gender": "male",
        "birthDate": "1990-09-15",
        "address": [
            {
                "use": "home",
                "line": [
                    "121212 Metcalf Drive",
                    "Apartment 403"
                ],
                "city": "Kansas City",
                "district": "Jackson",
                "state": "KS",
                "postalCode": "64199",
                "country": "United States of America",
                "period": {
                    "start": "2012-05-17T15:33:18.000Z"
                }
            }
        ],
        "maritalStatus": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
                    "code": "UNK",
                    "display": "Unknown"
                }
            ],
            "text": "Unknown"
        },
        "communication": [
            {
                "language": {
                    "coding": [
                        {
                            "system": "urn:ietf:bcp:47",
                            "code": "en",
                            "display": "English"
                        }
                    ],
                    "text": "English"
                },
                "preferred": True
            }
        ],
        "generalPractitioner": [
            {
                "reference": "Practitioner/4122622"
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()


patient_details = get_patient(12724067)
print("Fetched Patient Details ", patient_details)
search_result = search_patient("sma")
print("Fetched Patient Details via search", patient_details)
new_patient = create_new_patient()
print("New patient added", new_patient)

