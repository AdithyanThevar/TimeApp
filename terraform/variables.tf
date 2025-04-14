variable "aws_region" {
  default = "us-east-1"
}

variable "image_url" {
  description = "Docker image URL from DockerHub"
  type        = string
}
