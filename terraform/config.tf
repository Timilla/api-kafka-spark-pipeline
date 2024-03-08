# config.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Terraform Cloud configuration for GitHub Actions
  #  cloud {
  #    organization = "your_github_account"
  #
  #    workspaces {
  #      name = "gh-actions-datapipelines"
  #    }
  #  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
  profile = "stream_dsti"
}