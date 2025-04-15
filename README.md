# 🕒 TimeApp/SimpleTimeService

TimeApp is a simple application that returns the current server time and the client's IP address. It's deployed using **AWS ECS Fargate**, with **Terraform** for infrastructure provisioning and an **Application Load Balancer (ALB)** in front.

The purpose of this project is to:
- Deploy a scalable and isolated infrastructure for TimeApp
- Utilize AWS Fargate for serverless container hosting
- Demonstrate clean Infrastructure as Code (IaC) using Terraform modules
- Implement best practices like private subnets for app containers, NAT gateways, and ALB for routing

---

## 📁 Project Structure

    ├── app/                       # App source code and Docker-related files
    │   ├── app.py                 # Your Flask (or other) app
    │   ├── requirements.txt       # Python dependencies
    │   └── Dockerfile             # Container build config
    │
    ├── terraform/                 # Terraform configuration files
    │   ├── main.tf                # Main Terraform logic
    │   ├── variables.tf           # Input variables
    │   └── terraform.tfvars       # Variable values (optional)
    │
    └── README.md                  # You're here!

---

## ⚙️ Prerequisites

Before deployment, ensure the following tools are installed and configured:

- [Terraform](https://www.terraform.io/downloads) v1.3+
- [Docker](https://www.docker.com/) (for building/pushing the app image)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### ✅ Set Up AWS CLI

Make sure your AWS CLI is configured with the appropriate credentials before initializing Terraform.

To install, follow the official guide: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Then configure it using:

```bash
aws configure
```
When prompted, provide the following details:
- **AWS Access Key ID**: Your AWS access key
- **AWS Secret Access Key**: Your AWS secret key
- **Default region name**: Your preferred AWS region (e.g. `us-east-1`)
- **Default output format**: Leave as default (`json`)

---

## 🛠️ Deployment Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AdithyanThevar/TimeApp.git
cd TimeApp/terraform
```

### 2. Update Terraform Variables
Open `terraform.tfvars` file and edit the following lines according to your needs
```hcl
aws_region = "<your region>"
image_url  = "<your image URL>"
```

### 3. Initialize Terraform
Run the following command to initialize the Terraform configuration:
```bash
terraform init
```

### 4. Review the Plan
Before applying the configuration, review the Terraform plan to ensure everything is correct:
```bash
terraform plan
```

### 5. Apply the Configuration
Once you're satisfied with the plan, apply the configuration:
```bash
terraform apply
```

### 6. Get the Load Balancer DNS
After deployment, Terraform will output the ALB DNS name. Look for the following output:
```bash
Outputs: alb_dns_name = "http://<your-alb-dns-name>"
```

**You can now access your app:**

- Open the ALB DNS URL in your browser to see the app running, or
- Use `curl` to check the app from the command line:
```bash
curl http://<your-alb-dns-name>
```
