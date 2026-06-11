# 🎥 AI Video Assistant

> An intelligent AI-powered video assistant that helps users analyze, understand, and interact with video content using modern AI technologies.

---

## 📌 Overview

AI Video Assistant is a smart application that enables users to upload or provide video content and interact with it through AI. The system processes video data, extracts useful information, and provides intelligent responses, summaries, insights, or recommendations based on the video content.

---

## ✨ Features

- 🎬 Video Upload & Processing
- 📝 Automatic Transcript Generation
- 🤖 AI-Powered Question Answering
- 📚 Video Summarization
- 🔍 Semantic Search within Videos
- 💬 Interactive Chat Interface
- ⚡ Fast Response Generation
- 📊 Context-Aware Retrieval
- 🌐 User-Friendly Web Interface

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Frontend (Streamlit)
  │
  ▼
Backend API 
  │
  ├── Video Processing Module
  ├── Transcript Extraction
  ├── Embedding Generation
  ├── Vector Database
  └── LLM Inference Engine
  │
  ▼
AI Response Generation
  │
  ▼
User Interface
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit 

### Backend
- Python

### AI & Machine Learning
- LangChain
- Mistral
- Hugging Face Models

### Database
- ChromaDB

### Video Processing
- FFmpeg
- Whisper
- YouTube Transcript API

---

## 📂 Project Structure

```text
AI-Video-Assistant/
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarizer.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
│
├── requirements.txt
├── app.py
├── main.py
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Smart-Video-Assistant.git
cd AI-Video-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key
MODEL_NAME=your_model_name
VECTOR_DB_PATH=your_vector_db_path
```

---

## ▶️ Run the Application

```bash
uv streamlit run app.py
```

---

## 📖 Usage

1. Launch the application.
2. Upload a video or provide a video URL.
3. Wait for processing and transcript generation.
4. Ask questions about the video.
5. Receive AI-generated responses and summaries.

---

## 🧠 AI Workflow

```text
Video Input
     │
     ▼
Transcript Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
     │
     ▼
Vector Database Storage
     │
     ▼
Retriever
     │
     ▼
Large Language Model
     │
     ▼
Answer Generation
```

---

## 🔮 Future Improvements

- Multi-language support
- Real-time video analysis
- Speaker identification
- Video chapter generation
- Advanced analytics dashboard
- Voice-based interaction
- Multi-video knowledge base

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ankita Ghosh**

---

⭐ If you found this project useful, please consider giving it a star!
