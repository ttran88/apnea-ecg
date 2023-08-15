# Apnea Event Analysis Project

## Introduction
This project involves the development of algorithms using Python to analyze and score apnea events. The analysis is based on various signals such as ECGs, respiratory effort, oronasal airflow, and oxygen saturation. By converting clinical device-specific formatted flat files into an SQL database, this project streamlines the handling of essential data.

## Data Source
The data for this project is sourced from the Apnea-ECG Database, published by George Moody and Roger Mark.

**Publication Details:**
- Published: Feb. 10, 2000
- Version: 1.0.0
- Citation: T Penzel, GB Moody, RG Mark, AL Goldberger, JH Peter. The Apnea-ECG Database. Computers in Cardiology 2000;27:255-258.

**Data Description:**
The dataset consists of 70 records, divided into learning and test sets, with recordings varying in length from slightly less than 7 hours to nearly 10 hours each. File formats include .dat, .hea, .apn, and qrs, each serving different purposes.

For full data details and access, please visit the [Apnea-ECG Database page](#link-to-the-database).

## Methodology
1. **Data Ingestion:** Ingested and converted device-specific flat files (such as .dat, .hea, .apn, and qrs) into an SQL database for easy access and efficient management.
2. **Exploratory Analysis:** Performed analysis on continuous time series signals, including ECGs, respiratory signals, oronasal airflow, and oxygen saturation.
3. **Algorithm Development:** Utilized Python for the creation of algorithms to identify and score apnea events.
4. **Evaluation:** Assed the accuracy and effectiveness of different approaches to scoring apnea events, using both learning and test datasets.

## Requirements
- requirements.txt


## License
Please adhere to the original publication citation requirements when utilizing this resource.

## Acknowledgements
Special thanks to the creators and maintainers of the Apnea-ECG Database, and all those who contributed to this project.
