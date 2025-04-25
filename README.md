# 🛠️ **Multi-Functional Python Scripts**

Welcome to the **Multi-Functional Python Scripts** repository! This collection of Python scripts and Flask web applications showcases a variety of tools and utilities for file handling, API testing, NLP tasks, and more. Whether you're building web apps, processing PDFs, or automating data workflows, this repository has you covered.

## 🚀 **Key Features**

- **📁 File Handling**: Upload and download files using Flask.
- **📑 PDF Processing**: Extract data and text from PDF files.
- **🔄 JSON to Excel**: Convert JSON data into Excel for better reporting.
- **📧 SMTP Email Sending**: Send emails using SMTP servers.
- **⚙️ Environment Management**: Securely handle sensitive keys and assets.
- **📊 Data Handling with Pandas**: Convert lists to JSON with ease.
- **🧪 API Testing**: Test and ensure your APIs are working smoothly.
- **⚡ Auto GPU/CPU Selection**: Seamlessly switch between CPU and GPU for ML tasks.

## 📁 **Repository Contents**

Here’s an overview of the files included in this repository:

### 📝 **Scripts for Web Applications**
- **`flask_uploaded_files.py`**: A Flask app for uploading files through a web interface.
- **`download_files.py`**: Provides an API endpoint to download files hosted on the server.
- **`hosted_with_ngrok.py`**: Exposes your Flask app to the internet using Ngrok for quick sharing or testing.

### 💡 **Data & File Processing**
- **`json_to_excel.py`**: Convert JSON data into Excel files for reporting and data analysis.
- **`pandas_json_dump.py`**: Uses Pandas to convert Python lists into JSON and dumps the result to a file.
- **`pdf.py`**: A script to process and extract text from PDF files.

### ⚙️ **API Testing & Utilities**
- **`api_testing.py`**: A testing script to validate the functionality of your API endpoints.
- **`dot_env_.py`**: Manages sensitive environment variables, including keys and tokens.

### 📨 **Email Handling**
- **`smtp_handler.py`**: A utility for sending emails via SMTP servers.

### 📚 **Learning Resources**
- **`NLP_Course_on_Transformers.ipynb`**: A Jupyter notebook covering NLP fundamentals and transformer models using Hugging Face’s `transformers` library.

### 🖥️ **System Setup & Runtime**
- **`Set the runtime to cpu or gpu.py`**: Automatically switch between CPU and GPU based on system configuration.

## 🔧 **Setup Instructions**

### Prerequisites

- Python 3.10
- Flask
- Pandas
- Transformers (for NLP tasks)

### 1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/ravindrakush11/Multi-Functional-Python-Scripts-and-Flask-Web-Applications.git

cd Multi-Functional-Python-Scripts-and-Flask-Web-Applications
```

## ⚡ **Usage Instructions**

### 1. **Run Flask File Upload Example**
Launch the file upload API by running the following:

```bash
python flask_uploaded_files.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to upload files via the web interface.

### 2. **Run File Download API**
Start the Flask file download API with:

```bash
python download_files.py
```

The API will allow users to download files from the server.

### 3. **Expose Flask App Using Ngrok**
Make your Flask app accessible over the internet with:

```bash
python hosted_with_ngrok.py
```

Ngrok will generate a public URL for your local server.

### 4. **Explore NLP Course**
Open the **`NLP_Course_on_Transformers.ipynb`** Jupyter notebook to dive into NLP basics and explore transformer models from Hugging Face.

### 5. **PDF Text Extraction**
Process PDFs by running:

```bash
python pdf.py
```

This will enable you to extract text and data from PDFs.

### 6. **Convert JSON to Excel**
Use **`json_to_excel.py`** to convert JSON data into an Excel file:

```bash
python json_to_excel.py
```

### 7. **Send Emails via SMTP**
Send emails using **`smtp_handler.py`** by configuring SMTP settings and running the script:

```bash
python smtp_handler.py
```

### 8. **Switch Runtime for ML Tasks**
Use **`Set the runtime to cpu or gpu.py`** to automatically select the appropriate runtime:

```bash
python Set_the_runtime_to_cpu_or_gpu.py
```

## 💬 **Example API Usage**

To test the file upload and download functionality, use the following:

**File Upload Request (POST)**:

```bash
curl -X POST -F "file=@yourfile.txt" http://127.0.0.1:5000/upload
```

**File Download Request (GET)**:

```bash
curl -O http://127.0.0.1:5000/download/yourfile.txt
```

## 🤝 **Contributing**

We welcome contributions! Feel free to fork the repository, make improvements, and submit pull requests.

To contribute:
1. Fork the repository
2. Make your changes
3. Submit a pull request

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🚀 **Happy coding, and enjoy the tools!** ✨

