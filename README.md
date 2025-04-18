# DermaScan AI

An AI-powered dermatoscopic image analysis system that uses a deep learning model for skin lesion segmentation and ABCD feature extraction. The tool helps compute the Total Dermatoscopy Score (TDS) for melanoma risk evaluation and provides downloadable diagnostic reports via a web interface.

---

## Demo
The web app allows users to upload dermatoscopic skin lesion images and view segmentation overlays, ABCD metrics, and final TDS scores. A downloadable PDF report is also generated.



To try it locally, follow the steps below to set up the project.

---

## Installation
This project was tested on macOS and AWS EC2 Ubuntu 20.04 instances.

### Requirements
- Python 3.10+
- Git
- Virtual environment tools
- AWS CLI (for cloud uploads)

### Setup Instructions
```bash
git clone https://github.com/your-org/dermascan-ai.git
cd dermascan-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Dependencies (in `requirements.txt`)
- flask
- torch
- torchvision
- torchaudio
- opencv-python
- numpy
- reportlab
- boto3

### ⚠️ Model File
Due to size limits, the trained segmentation model is stored **locally** and not published online. Request access from the team and place the model file in the `models/` folder before launching.

---

## 🔁 Reproducing the Project

### Uploading Image Data to S3
```bash
aws s3 cp "/path/to/local/images" s3://your-s3-bucket/input/ --recursive
```

### EC2 Setup
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv awscli git
```

```bash
git clone https://github.com/your-org/dermascan-ai.git
cd dermascan-ai
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Launching the Web App
```bash
python3 app.py
```

---

## Evaluation
To evaluate segmentation or feature extraction results:
```bash
python evaluate_abcd.py --images=./data/test --output=./results
```

---

## 📦 Project Structure
```
dermascan-ai/ ├── scripts/ # Optional shell/utility scripts
├── src/ # Core backend and analysis logic
├── static/ # Static files (CSS, images)
├── templates/ # HTML templates for Flask
├── app.py # Flask entry point
├── abcd_analysis.py # ABCD feature extraction script
├── color_score.py # Color feature analysis
├── hyper_tune.py # Hyperparameter tuning tools
├── requirements.txt # Python dependencies
├── LICENSE # License file
├── README.md # This file
```


