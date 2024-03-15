# Mock Service : Mock Patient Health Record Service
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


# Module 1 : Fetching data from heath records (mock)
* 		get_patient(patient_id):
    * Description: Retrieves the information of a patient with the specified ID.
  		* Parameters:
      * patient_id (int): The ID of the patient to retrieve information for.
    * Returns: A dictionary containing the patient's information.
    * Example Usage:
      * ```patient_details = get_patient(12724067)```

* 		search_patient(search_text):
    * Description: Searches for patients whose information matches the specified search text.
    * Parameters:
      * search_text (str): The text to use for searching patient information.
    * Returns: A list of dictionaries, each containing the information of a patient that matches the search text.
    * Example Usage:
     * ```search_result = search_patient("sma")```


* 		create_new_patient():
    * Description: Creates a new patient record in the FHIR server with mock data.
    * Returns: A success code indicating the new patient record creation.
    * Example Usage:
      * ```new_patient = create_new_patient()```


* cmd to execute this file :  python data/patient.py


# Module 2 : Fetching data from EHR and pushing to UM (mocking), processing to calculate score for eacg record
* 		calculate_medical_score(health_record):
    * Description: Calculates a medical score based on a patient's health record.
        * Parameters:
        * health_record (dict): The health record of a patient, including blood pressure, prescriptions, problems, and progress notes.
    * Returns: An integer representing the medical score.
* 		process_heath_record():
    * Description: Processes a user's health record to extract relevant information.
    * Returns: A dictionary containing the user's name, email address, number of problems in their health record, number of prescriptions, and medical score.
* 		update_health_record(id):
    * Description: Updates the health record of a patient with the specified ID.
        * Parameters:
        * id (int): The ID of the patient whose health record is to be updated.
    * Returns: The updated health record.
* 		submit_prescriptions(patient_id):
    * Description: Submits new prescriptions for a patient with the specified ID.
        * Parameters:
        * patient_id (int): The ID of the patient to submit prescriptions for.
    * Returns: A dictionary containing the updated prescription information.
* 		check_coverage(medical_score):
    * Description: Checks if the medical score is above a certain threshold for insurance coverage approval.
        * Parameters:
        * medical_score (int): The medical score of a patient.
    * Returns: A tuple containing a boolean indicating whether coverage is approved and a message explaining the decision.

* cmd to execute the file :  python data/ehr_to_um.py

