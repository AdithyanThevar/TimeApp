## 🕒 TimeApp

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

### 🐳 Docker Hub
```bash
# Tag with your username
docker tag timeapp:latest <your-dockerhub-username>/timeapp:latest

# Login to Docker Hub
docker login

# Push image
docker push <your-dockerhub-username>/timeapp:latest
```

## 🚀 Deployment Instructions

After pushing your image to the registry:

1. Update the Terraform configuration in Terraform directory:
       
```bash
vi TimeApp/terraform/terraform.tfvars
```

   Set the correct image URL based on your registry:
```hcl
container_image = "<your-username>/timeapp:latest"
```

2. Deploy the infrastructure:
```bash
cd TimeApp/terraform
terraform init         
terraform plan         
terraform apply   
```
3. Access your application:
    - The Load Balancer URL will be shown in Terraform outputs
    - Run terraform output alb_dns_name to view it anytime

**Note: The default configuration uses adithyanthevar/timeapp if no changes are made to terraform.tfvars.**