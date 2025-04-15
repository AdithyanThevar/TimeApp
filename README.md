# 🕒 TimeApp/SimpleTimeService

TimeApp is a simple application that returns the current server time and the client's IP address. It's deployed using **AWS ECS Fargate**, with **Terraform** for infrastructure provisioning and an **Application Load Balancer (ALB)** in front.

The purpose of this project is to:
- Deploy a scalable and isolated infrastructure for TimeApp
- Utilize AWS Fargate for serverless container hosting
- Demonstrate clean Infrastructure as Code (IaC) using Terraform modules
- Implement best practices like private subnets for app containers, NAT gateways, and ALB for routing

---

## 📁 Project Structure

├── main.tf # Main Terraform configuration ├── variables.tf # Input variables ├── outputs.tf # Output values (e.g., ALB DNS) ├── terraform.tfvars # Variable values (optional) ├── docker/ # Dockerfile for TimeApp container │ └── Dockerfile ├── app/ # App source code (Go / Node.js / Python) │ └── main.go | app.py | index.js └── README.md # You're here!


---

## ⚙️ Prerequisites

Before deployment, ensure the following tools are installed and configured:

- [Terraform](https://www.terraform.io/downloads) v1.3+
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) with credentials configured
- [Docker](https://www.docker.com/) (for building/pushing the app image)
- An AWS ECR repository (if you're using your own image)

---

## 🛠️ Deployment Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AdithyanThevar/TimeApp.git
cd TimeApp/terraform
```

### 2. Update Terraform Variables

Edit `variables.tf` or create a `terraform.tfvars` file and add the following:

```hcl
aws_region = "us-east-1"
image_url  = "your-ecr-image-url"
```