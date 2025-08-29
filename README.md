# FastAPI Hello World v2

A simple FastAPI hello world application with enhanced features and proper project structure.

## 🚀 Features

- **FastAPI** - Modern, fast (high-performance) web framework for building APIs
- **Automatic Documentation** - Interactive API docs with Swagger UI
- **Health Checks** - Built-in health monitoring endpoint
- **Dockerized** - Ready for containerized deployment
- **Type Hints** - Full type annotation support with Pydantic
- **Enhanced Endpoints** - Multiple endpoints with different functionalities

## 📋 Requirements

- Python 3.11+
- FastAPI 0.104.1+
- Uvicorn for ASGI server

## 🛠️ Installation

### Option 1: Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arch-faustocorrea/fastapi-hello-world-v2.git
   cd fastapi-hello-world-v2
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

### Option 2: Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t fastapi-hello-world-v2 .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 fastapi-hello-world-v2
   ```

## 🌐 API Endpoints

Once running, the application will be available at `http://localhost:8000`

### Available Endpoints:

- **`GET /`** - Root hello world endpoint
- **`GET /hello/{name}`** - Personalized greeting
- **`GET /health`** - Health check endpoint
- **`GET /info`** - Application information
- **`GET /docs`** - Interactive API documentation (Swagger UI)
- **`GET /redoc`** - Alternative API documentation

## 📊 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🧪 Example Usage

### Basic Hello World
```bash
curl http://localhost:8000/
```
Response:
```json
{
  "message": "Hello World from FastAPI v2!",
  "timestamp": "2025-08-29T15:30:00.123456",
  "version": "2.0.0"
}
```

### Personalized Greeting
```bash
curl http://localhost:8000/hello/Fausto
```
Response:
```json
{
  "message": "Hello Fausto! Welcome to FastAPI v2",
  "timestamp": "2025-08-29T15:30:00.123456",
  "version": "2.0.0"
}
```

### Health Check
```bash
curl http://localhost:8000/health
```
Response:
```json
{
  "status": "healthy",
  "timestamp": "2025-08-29T15:30:00.123456"
}
```

## 📁 Project Structure

```
fastapi-hello-world-v2/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── .gitignore         # Git ignore rules
```

## 🔧 Development

### Running in Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Environment Variables
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

## 🐳 Docker Deployment

The application includes a multi-stage Dockerfile for efficient containerization:

- **Base Image:** Python 3.11 slim
- **Port:** 8000
- **Health Check:** Built-in health monitoring
- **Production Ready:** Optimized for deployment

## 🚀 Deployment Options

### Local Development
```bash
uvicorn main:app --reload
```

### Production with Uvicorn
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Production
```bash
docker run -d -p 8000:8000 --name fastapi-app fastapi-hello-world-v2
```

## 📋 Version Information

- **Version:** 2.0.0
- **FastAPI Version:** 0.104.1+
- **Python Version:** 3.11+

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏢 About

Part of the AI Workstream - Data Playground project by Architech.

**Author:** Fausto Correa  
**Email:** fcorrea@architech.ca  
**Project:** AI Workstream - Data Playground (AWDP)
