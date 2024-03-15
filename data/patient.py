import requests


def get_patient(patient_id):

    url = f"http://127.0.0.1:5000/api/patient/{patient_id}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to Fetch Response"


def search_patient(search_text):
    url = f"http://127.0.0.1:5000/api/patient?search={search_text}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "No record found"

def create_new_patient():
    import requests
    import json

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

    print(response.json())

print(get_patient(12724067))
print(search_patient("sma"))

print(create_new_patient())

