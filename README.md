# Protecting Intellectual Security Through Hate Speech Detection Using Artificial Intelligence Approaches 
This project is part of my thesis: "Protecting Intellectual Security Through Hate Speech Detection Using Artificial Intelligence Approaches". It focuses on identifying and classifying hate speech in Arabic text to promote safer and more secure communication.
# Project Overview
This project aims to collect Arabic datasets from the social media platform X and develop a two-layer framework for detecting Arabic hate speech. The framework will classify the hate speech into specific types (Religious, Political or Social Hate speech ) using deep learning and machine learning techniques. The proposed framework aims to improve detection accuracy.
# Repository Structure
* ALL about dataset:
The ALL about dataset folder contains all the files related to the dataset creation, preprocessing, and annotation for Arabic hate speech detection:

1-data by keyword: Raw data grouped by specific keywords used during data extraction.
2-Annotation guideline.pdf: Instructions provided to annotators for labeling the dataset consistently.
3-Annotaton results.xlsm: Detailed annotation results, including text samples and their corresponding labels.
4-all_data.xlsx: The complete dataset before any preprocessing.
5-dataset after preprocessed.xlsx: The dataset after cleaning and preprocessing steps, such as removing unnecessary data or formatting text.
6-dataset after tokenization.xlsx: The dataset after text tokenization, prepared for machine learning models.

* Hate Speech Detection (First Layer):
This layer detects whether a piece of text contains hate speech.
We utilized machine learning (ML) and deep learning (DL) models to perform this task. Various techniques were employed for feature extraction and word embeddings.

* Hate Speech Classification (Second Layer):
Once hate speech has been detected in the first layer, this second layer classifies it into specific categories based on its type (Religious, Political or Social) Hate speech

