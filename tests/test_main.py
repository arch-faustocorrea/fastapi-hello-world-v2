import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMainEndpoints:
    """Test cases for main application endpoints"""
    
    def test_read_root(self):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello World from FastAPI v2!"
        assert data["version"] == "2.0.0"
        assert "timestamp" in data

    def test_say_hello_valid_name(self):
        """Test the personalized hello endpoint with valid name"""
        response = client.get("/hello/Fausto")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello Fausto! Welcome to FastAPI v2"
        assert data["version"] == "2.0.0"
        assert "timestamp" in data

    def test_say_hello_empty_name(self):
        """Test the personalized hello endpoint with empty name"""
        response = client.get("/hello/")
        # This should return 404 due to path parameter requirement
        assert response.status_code == 404

    def test_say_hello_whitespace_name(self):
        """Test the personalized hello endpoint with whitespace name"""
        response = client.get("/hello/%20")  # URL encoded space
        assert response.status_code == 400
        data = response.json()
        assert data["detail"] == "Name cannot be empty"

    def test_health_check(self):
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data

    def test_get_info(self):
        """Test the application info endpoint"""
        response = client.get("/info")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "FastAPI Hello World v2"
        assert data["version"] == "2.0.0"
        assert "endpoints" in data
        assert isinstance(data["endpoints"], list)
        assert "/" in data["endpoints"]
        assert "/health" in data["endpoints"]

    def test_docs_endpoint(self):
        """Test that the docs endpoint is accessible"""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

    def test_openapi_endpoint(self):
        """Test that the OpenAPI spec endpoint is accessible"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert data["info"]["title"] == "FastAPI Hello World v2"
        assert data["info"]["version"] == "2.0.0"

class TestErrorHandling:
    """Test cases for error handling"""
    
    def test_non_existent_endpoint(self):
        """Test accessing a non-existent endpoint"""
        response = client.get("/non-existent")
        assert response.status_code == 404

    def test_method_not_allowed(self):
        """Test using wrong HTTP method"""
        response = client.post("/")
        assert response.status_code == 405

class TestResponseFormat:
    """Test cases for response format validation"""
    
    def test_root_response_structure(self):
        """Test that root endpoint returns expected structure"""
        response = client.get("/")
        data = response.json()
        
        # Check required fields
        required_fields = ["message", "timestamp", "version"]
        for field in required_fields:
            assert field in data
        
        # Check data types
        assert isinstance(data["message"], str)
        assert isinstance(data["version"], str)
        assert isinstance(data["timestamp"], str)

    def test_hello_response_structure(self):
        """Test that hello endpoint returns expected structure"""
        response = client.get("/hello/TestUser")
        data = response.json()
        
        # Check required fields
        required_fields = ["message", "timestamp", "version"]
        for field in required_fields:
            assert field in data
        
        # Check that name is included in message
        assert "TestUser" in data["message"]

    def test_health_response_structure(self):
        """Test that health endpoint returns expected structure"""
        response = client.get("/health")
        data = response.json()
        
        # Check required fields
        required_fields = ["status", "timestamp"]
        for field in required_fields:
            assert field in data
        
        # Check values
        assert data["status"] == "healthy"
