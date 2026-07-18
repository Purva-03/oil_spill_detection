# 🛢️ OilSense – Oil Spill Detection and Classification System

## 📌 Overview

OilSense is an AI-powered Oil Spill Detection and Classification System designed to analyze aerial and SAR (Synthetic Aperture Radar) imagery for identifying oil spills on ocean surfaces.

The system leverages Deep Learning-based Semantic Segmentation to detect and classify sea-surface regions into multiple categories, estimate spill area and volume, classify oil type, assess environmental risk levels, and generate analytical reports.

The application is built using **PyTorch**, **Segmentation Models PyTorch (SMP)**, and **Streamlit** for an interactive web-based interface.

---

## 🚀 Features

### 🔍 Oil Spill Detection

* Detects oil spills from SAR/Aerial images.
* Pixel-wise semantic segmentation.
* High-resolution visual overlays.

### 🧠 Deep Learning Model

* DeepLabV3+ Architecture
* EfficientNet-B3 Encoder
* Multi-class segmentation

### 📊 Oil Classification

Classifies detected regions into:

| Class | Description           |
| ----- | --------------------- |
| 0     | Background / Sea      |
| 1     | Oil Spill             |
| 2     | Look-alike Phenomenon |
| 3     | Ship / Object         |

---

### 🌊 Oil Type Identification

The system estimates oil appearance and thickness:

* Silver Sheen
* Rainbow Sheen
* Brown Oil
* Black / Red Oil
* Mixed Oil

---

### 📏 Spill Area Estimation

Calculates:

* Oil Pixel Count
* Percentage Coverage
* Estimated Spill Area (km²)

---

### 🛢️ Volume Estimation

Volume is estimated using:

Volume = Area × Thickness

Outputs:

* Estimated Oil Volume (m³)



### 📈 Interactive Analytics Dashboard

Includes:

* Oil Probability Heatmap
* Class Distribution Pie Chart
* Confidence Analysis
* Contour Detection
* Overlay Visualization

---

### 📄 Automatic Incident Reports

Generates downloadable reports containing:

* Detection Results
* Spill Area
* Volume Estimation
* Oil Type
* Confidence Score
* Risk Assessment

---

### 🧠 GAN Integration

The system supports visualization of GAN-generated SAR images produced during training.

Features:

* Google Drive Integration
* Epoch-wise Generated Images
* Real vs Generated Comparison

---

## 🏗️ System Architecture

```text
Input SAR/Aerial Image
          │
          ▼
    Preprocessing
          │
          ▼
 DeepLabV3+ Segmentation
(EfficientNet-B3 Encoder)
          │
          ▼
 Multi-Class Prediction
          │
          ├────────► Oil Classification
          │
          ├────────► Area Calculation
          │
          ├────────► Volume Estimation
          │
          ├────────► Risk Assessment
          │
          ▼
  Visualization & Reports
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Deep Learning

* PyTorch
* Segmentation Models PyTorch (SMP)

### Image Processing

* OpenCV
* NumPy

### Visualization

* Plotly
* Matplotlib

### Deployment

* Streamlit Web App
## 📸 Workflow

1. Upload SAR or Aerial Image
2. Model performs semantic segmentation
3. Oil spill regions are detected
4. Oil type is classified
5. Spill area is calculated
6. Oil volume is estimated
7. Risk level is generated
8. Interactive dashboard displays results
9. Download incident report


## 🎯 Applications

* Marine Pollution Monitoring
* Offshore Oil Leak Detection
* Coastal Surveillance
* Environmental Protection Agencies
* Maritime Safety
* Disaster Response Systems

---

## 🔮 Future Enhancements

* Real-Time Satellite Data Integration
* AIS Ship Tracking
* Multi-Spectral Analysis
* Transformer-based Segmentation Models
* Cloud Deployment (AWS/Azure)
* Mobile Application Support
* Automatic Alert System

---


## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
