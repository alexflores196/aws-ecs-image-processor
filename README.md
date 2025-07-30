# AWS Cloud Image Processor: A Serverless, Auto-Scaling Web Application

A comprehensive, cloud-native web application built on AWS that allows users to upload images, view detailed metadata, perform conversions, and download the results. This project demonstrates a secure, highly available, and event-driven architecture with a fully automated CI/CD pipeline for deployments.

## Architecture Diagram

_To create your own diagram, I highly recommend using a free tool like_ [_**diagrams.net**_](https://app.diagrams.net/ "null") _(formerly draw.io). You can create a diagram that looks like the one below and export it as a `.png` to include here._

_(Replace the link above with a link to your own architecture diagram image)_

## Key Features

-   **Session-Based User Experience**: Each user gets a private, temporary workspace. Images are isolated per session and automatically cleaned up after 24 hours using S3 Lifecycle Policies.
    
-   **Advanced Image Processing**:
    
    -   **Automatic Thumbnail Generation**: An event-driven AWS Lambda function instantly creates thumbnails upon image upload.
        
    -   **Detailed Metadata Extraction**: The Lambda function extracts and stores both basic (size, format) and enhanced EXIF (camera model, settings) metadata in DynamoDB.
        
    -   **On-the-Fly Conversion**: Users can convert images to various popular formats (JPG, PNG, WEBP, etc.) and resize them to custom dimensions before downloading.
        
-   **High Availability & Auto-Scaling**: The application is deployed on **ECS Fargate**, a serverless container engine, across multiple Availability Zones. It automatically scales the number of running tasks based on CPU utilization to handle traffic spikes efficiently.
    
-   **Robust Security**:
    
    -   **Network Isolation**: All resources are deployed within a custom, secure Amazon VPC with public and private subnets.
        
    -   **Web Application Firewall (WAF)**: An AWS WAF is attached to the Application Load Balancer to protect against common web threats like SQL injection and cross-site scripting.
        
    -   **Principle of Least Privilege**: IAM roles are finely tuned to grant each service only the permissions it needs to function.
        
-   **Fully Automated CI/CD Pipeline**:
    
    -   A multi-stage **AWS CodePipeline** automates the entire deployment process.
        
    -   Pushing code to the `main` branch on GitHub automatically triggers **AWS CodeBuild**.
        
    -   CodeBuild builds the Docker image for the web app and the deployment package for the Lambda function in parallel.
        
    -   The pipeline then automatically deploys the new versions to Amazon ECS and AWS Lambda with zero downtime.
        
-   **Infrastructure as Code (IaC)**: The core network, security, and database infrastructure is defined declaratively using **AWS CloudFormation**, enabling consistent and repeatable environment creation.
    

## Technology Stack

| Category | Technology / Service |

| Compute | AWS Fargate (for ECS), AWS Lambda |

| Storage | Amazon S3, Amazon DynamoDB |

| Networking & Security | Amazon VPC, Application Load Balancer, AWS WAF, IAM |

| CI/CD Pipeline | AWS CodePipeline, AWS CodeBuild, AWS CodeStar Connections, Amazon ECR, GitHub |

| Application & Framework | Python, Flask, Pillow (PIL) |

| Infrastructure as Code | AWS CloudFormation |

| Monitoring & Logging | Amazon CloudWatch |

## Project Structure

The repository is organized into distinct components, reflecting a professional microservice-oriented structure.

```
.
├── application/
│   ├── Dockerfile          # Defines the main web application container
│   ├── app.py              # The Flask web server and API logic
│   ├── buildspec.yml       # Build instructions for the CI/CD pipeline
│   ├── requirements.txt    # Python dependencies for the web app
│   └── templates/
│       └── index.html      # Front-end HTML template
└── lambda/
    ├── lambda_function.py  # Python code for the image processing Lambda
    ├── buildspec.yml       # Build instructions for the Lambda function
    └── requirements.txt    # Python dependencies for the Lambda function


```

## Setup and Deployment

This project is fully automated via the CI/CD pipeline. The initial infrastructure setup is done once with CloudFormation, and all subsequent application deployments are handled by pushing to the `main` branch on GitHub.

### Initial Infrastructure Setup (One-Time)

1.  **Prerequisites**: AWS CLI installed and configured, Docker installed.
    
2.  **Deploy CloudFormation Stack**: Deploy the `infrastructure/template.yml` file via the AWS CloudFormation console. This will create the VPC, S3 bucket, DynamoDB table, and all necessary IAM roles and security groups.
    
3.  **Create CI/CD Pipeline**: Create the AWS CodePipeline as detailed in the project documentation, connecting it to this GitHub repository and configuring the CodeBuild and deployment stages.
    

### Automated Deployment (For all code changes)

1.  Commit and push your code changes to the `main` branch of this repository.
    
2.  The push will automatically trigger the CodePipeline.
    
3.  The pipeline will build, test, and deploy the new versions of the ECS service and Lambda function.
