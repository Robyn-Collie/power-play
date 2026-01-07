provider "aws" {
  region = "us-east-1"
}

# Example VPC for Enterprise Deployment
resource "aws_vpc" "power_move_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "power-move-vpc"
  }
}

# ECS Cluster for AI Services
resource "aws_ecs_cluster" "ai_cluster" {
  name = "power-move-ai-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

# Placeholder for ECR Repository
resource "aws_ecr_repository" "backend_repo" {
  name                 = "power-move-backend"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
