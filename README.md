# Step 1 : Mock Patient Health Record Service
 This service provides mock data related to patient health records. It includes endpoints for creating a patient record, retrieving a patient record by ID, and searching for patient records.

### Endpoints
####  1. Create Patient Record
- URL: /api/patient
- Method: POST
- Description: Creates a new patient record.
- Request Body: None
- Response: JSON containing the ID of the newly created patient record.

#### 2. Retrieve Patient Record
- URL: /api/patient/<patient_id>
- Method: GET
- Description: Retrieves a patient record by ID.
- Response: JSON containing the patient record details.

#### 3. Search Patient Records
- URL: /api/patient
- Method: GET
- Description: Searches for patient records based on query parameters.
- Response: JSON containing a list of patient records matching the search criteria.

## Running the Mock Patient Health Record Service

  -  ```{ pip install flask }```
  - To run the service, execute the Python script. By default, the service runs in debug mode
    - python data/mock_server.py


**Note** : This service provides mock data and is intended for development and testing purposes only

**Reference** : https://fhir.cerner.com/millennium/r4/base/individuals/patient

