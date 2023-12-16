# Algorithms and Data Structures Phase-1: Doubly Linked Lists

This repository is part of an educational series for an Algorithms and Data Structures class, focusing on doubly linked lists and their use in managing health center data, including patient records.

## About The Project

The project includes implementations of doubly linked lists (DList) and demonstrates their use in a practical application — managing health center data. It allows for patient records to be added in alphabetical order, searched based on certain criteria, and provides statistics on the data.

### Modules

- `dlist.py`: Contains the implementation of a generic doubly linked list.
- `fase1.py`: Extends `dlist.py` with a specialized `HealthCenter` class for managing patient data.
- `unittest-fase1.py`: Provides a suite of unit tests to ensure the correctness of the classes and methods.

## Usage

The `HealthCenter` class can be used to create a health center object, add patients, search for patients based on criteria, and compute statistics:

```
from fase1 import HealthCenter, Patient

# Create a HealthCenter object
health_center = HealthCenter('path_to_tsv_file.tsv')

# Add a new patient
patient = Patient('Doe, John', 1990, False, 1)
health_center.addPatient(patient)

# Search for patients based on criteria
patients = health_center.searchPatients(year=1990, covid=False, vaccine=1)

# Compute statistics
stats = health_center.statistics()

```

## Contact

Rosa Reyes: [LinkedIn](https://www.linkedin.com/in/rosaareyesc/)
