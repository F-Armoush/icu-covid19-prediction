# Raw Data
This project uses the Hospital Sírio-Libanês COVID-19 ICU Prediction dataset.

## Dataset License
The dataset is distributed under the following license:
* CC BY-NC 4.0
* https://creativecommons.org/licenses/by-nc/4.0/

## Attribution
Dataset source:
* Hospital Sírio-Libanês / Kaggle COVID-19 ICU Prediction Dataset

## Accessing the Dataset
The original raw dataset is included in this repository under:

```
data/raw/
```

Alternatively, the dataset can be downloaded from its original public source:

* [Kaggle - COVID-19 ICU Prediction Dataset](https://www.kaggle.com/datasets/S%C3%ADrio-Liban%C3%AAs/covid19?utm_source=chatgpt.com)


## Processed Dataset

The processed modeling dataset generated during preprocessing is stored in:

```
data/processed/
```

File:

```
df_model.csv
```

This processed dataset:

* uses one row per patient
* contains only the first observation window (0–2 hours)
* is structured to prevent temporal leakage
* is used for all training and evaluation experiments



## Notes

* The processed dataset (`df_model.csv`) was generated from the original raw dataset during preprocessing.
* This repository is intended for educational, research, and portfolio purposes only.
