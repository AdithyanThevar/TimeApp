## 🕒 TimeApp Deployment

A simple Flask application that returns the client's IP and current UTC timestamp. Containerized with Docker and deployable via Terraform to AWS ECS.

## Features
- Returns client IP address 
- Returns current UTC timestamp
- Lightweight Python/Flask implementation
- Secure Docker configuration (non-root user)

## 📁 Project Structure

    ├── app/                       
    │   ├── app.py                 
    │   ├── requirements.txt       
    │   ├── Dockerfile             
    │   └── README.md              # You're here!
    |
    ├── terraform/                 
    │   ├── main.tf                
    │   ├── variables.tf           
    │   └── terraform.tfvars       
    │
    └── README.md                  

## 📋 Prerequisites
- Docker installed
- AWS account with CLI configured
- Terraform v1.3+ installed

## 🛠️ Local Development with Docker
```bash
docker build -t timeapp:latest .
```

## ⚙  Test the application locally
```bash
docker run -d -p 9000:9000 --name timeapp timeapp:latest
curl http://localhost:9000
```

## 📦 Push to Registry

Using Pre-built Image (Quick Start)

A pre-built image is available at adithyanthevar/timeapp on Docker Hub. The Terraform configuration uses this by default.

### Option A: 🐳 Docker Hub
```bash
# Tag with your username
docker tag timeapp:latest <your-dockerhub-username>/timeapp:latest

# Login to Docker Hub
docker login

# Push image
docker push <your-dockerhub-username>/timeapp:latest
```

### Option B: ☁️ Push to AWS ECR

```bash
# 1. Authenticate with ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# 2. Create repository (first time only)
aws ecr create-repository \
    --repository-name timeapp \
    --image-scanning-configuration scanOnPush=true \
    --image-tag-mutability MUTABLE

# 3. Tag your image
docker tag timeapp:latest <account-id>.dkr.ecr.<region>.amazonaws.com/timeapp:latest

# 4. Push image to ECR
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/timeapp:latest
```