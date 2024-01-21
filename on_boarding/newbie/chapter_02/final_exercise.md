# Day 08 - Embracing DevOps: GitLab, SSH, Docker, and CI/CD Pipeline 🚀

## Overview

**Goals:**

- Introduce the concept of Continuous Integration and Continuous Deployment (CI/CD) using GitLab.
- Learn how to set up SSH authorization for secure interaction with the repository.
- Understand the process of building Docker images and pushing them to a Docker registry.
- Implement a CI/CD pipeline for automating the build, test, and deployment processes.

**⚠️ Note:**

- CI/CD is a crucial aspect of the modern development workflow. It brings automation, consistency, and quality control to your projects.
- Familiarize yourself with GitLab's interface and features as it will be an integral part of your development process.
- Ensure Docker is correctly set up on your machine and you have access to Docker.io to push and pull images.

**Total Time:** 8 hours

## Chapter 1: GitLab and SSH Authorization

**Est. Time: 1.5 hours**

### Tasks

1. **Create a New Repository on GitLab:**
   - Initialize a new GitLab repository named "The_Last_Airbender" at [GitLab](https://gitlab.com/).
   - Clone the repository to your local machine to start working on the project.

2. **SSH Key Setup and Authorization:**
   - Generate an SSH key pair on your local machine if you haven't already.
   - Add the public SSH key to your GitLab account for secure and password-less communication with the repository.
   - After establishing SSH authorization, connect to your repo via SSH.

3. **Adding 'The_Last_Airbender' Files to the Project:**
   - Ensure that the project's repository is correctly cloned to your local machine.
   - Add the files related to ["the_last_air_bender"](./the_last_air_bender/README.md) into the cloned project directory.
   - Commit and push the changes to the GitLab repository.

## Chapter 2: Docker Introduction and Image Creation

**Est. Time: 1.5 hours**

### Core Concepts

1. **Docker Overview:**
   - Understand the fundamentals of Docker and how it encapsulates applications and their environments using containers.

2. **Writing a Dockerfile:**
   - Create a Dockerfile for the Python application. Define the base image, set up the environment, copy the application code, and specify the entry command.

3. **Building and Testing the Docker Image:**
   - Build the Docker image from the Dockerfile.
   - Test the Docker image locally to ensure the application runs as expected.

4. **Pushing to Docker.io:**
   - Tag the Docker image with the appropriate version number and repository name.
   - Push the Docker image to your Docker.io registry to make it available for deployment.

## Chapter 3: Implementing CI/CD with GitLab

**Est. Time: 4 hours**

### Core Concepts and Tasks

1. **CI/CD Pipeline Overview:**
   - Understand the stages of a CI/CD pipeline: Build, Test, and Deploy.

2. **Creating `.gitlab-ci.yml`:**
   - Write the `.gitlab-ci.yml` file defining the CI/CD pipeline configuration.
   - Specify the stages, scripts, and conditions for each stage of the pipeline.

3. **Build Stage:**
   - Configure the pipeline to build the Docker image from the Dockerfile.
   - Ensure the image is built correctly and is ready for testing and deployment.

4. **Test Stage:**
   - Run the predefined tests in the repository to ensure the code meets the quality standards.
   - Use PyTest for executing the test cases in the Python application.

5. **Deploy Stage:**
   - Push the successfully built and tested Docker image to Docker.io.
   - (Optional) Define deployment steps if you have a specific environment to deploy the application.

## Wrapping Up the Day

**Reflection and Planning (30 minutes):**

- Review the CI/CD pipeline's execution and ensure every stage completes successfully.
- Plan any further enhancements or optimizations you might want to introduce to the pipeline.

Congratulations on completing Day 08! You've successfully set up a complete CI/CD pipeline, paving the way for efficient, automated, and reliable development workflows.
