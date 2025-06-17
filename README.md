[![CI/CD for MCP Server](https://github.com/sagar0x0/auto-deploy-mcp-server-2/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/sagar0x0/auto-deploy-mcp-server-2/actions/workflows/ci-cd.yml)


# Automated CI/CD Pipeline to deploy mcp-server

This repository showcases a fully automated CI/CD pipeline for containerized Python applications using **GitHub Actions** and **Kubernetes** (via **Minikube**). It automates building, testing, and deployment workflows for both staging and production environments, with security scanning integrated into every run.

---

## 🔧 Features

* **Continuous Integration (CI)**
  Automatically builds and tests the application on every push or pull request to the `main` branch.

* **Automated Security Scanning**
  Integrates **GitHub CodeQL** to scan Python code for known vulnerabilities during CI workflows.

* **Staging Deployments**
  Each pull request is automatically deployed to a **staging** environment for validation before merging.

* **Continuous Deployment (CD)**
  Once merged to `main`, the latest version is automatically deployed to a **production** environment.

* **Self-Hosted Runner Integration**
  Deployment steps run on a self-hosted runner with **Minikube** and **Docker** installed.

---

## ⚙️ How It Works

The CI/CD pipeline is defined in `.github/workflows/ci-cd.yml` and is structured around two key workflows:

### 1. ✅ Pull Request Workflow

Triggered when a pull request is opened against the `main` branch.

#### 🔍 CI: Build, Test & Security Scan

*Executed on a GitHub-hosted runner*

* Checkout code
* Install dependencies
* Run unit tests
* Perform **CodeQL** security scanning

#### Deploy to Staging

*Executed on a self-hosted runner*

* Start **Minikube**
* Build a Docker image of the application
* Deploy to a staging namespace in the cluster using Kubernetes manifests

✅ The pull request must pass both jobs to be eligible for merge.

---

### 2. Merge Workflow (Production Deployment)

Triggered when changes are merged into the `main` branch.

#### 🔄 CI: Rebuild & Rescan

Ensures merged code is still valid and secure.

#### 📦 Deploy to Production

*Executed on a self-hosted runner*

* Start **Minikube**
* Build the final `:latest` Docker image
* Apply Kubernetes manifests to deploy to the **production** environment
* Output running services for confirmation

---

## 📁 Repository Structure

```
.
├── .github/workflows/
│   └── ci-cd.yml            # CI/CD workflow configuration
│
├── app/
│   └── mcp-server/
│       ├── app/
│       │   └── mcp_server.py      # Main Python application
│       ├── Dockerfile             # Docker build instructions
│       ├── k8s/
│       │   └── deployment.yaml    # Kubernetes deployment/service config
│       ├── requirements.txt       # Python dependencies
│       └── tests/
│           └── test_mcp_server.py # Unit tests
│
└── README.md
```

---

## Getting Started

### Prerequisites

Ensure your self-hosted runner is configured with the following:

* [Docker](https://docs.docker.com/)
* [Minikube](https://minikube.sigs.k8s.io/docs/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)

### Setup Instructions

1. **Fork this Repository**
   Create a fork in your GitHub account to get started.

2. **Configure a Self-Hosted Runner**
   Follow [GitHub’s guide](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) to add a self-hosted runner.

   > Ensure your runner has the `self-hosted` label—this is required for deployment jobs.

3. **Add Your Application Code**
   Replace the contents of `app/mcp-server/` with your own Python application.

4. **Update Configuration Files**

   * Modify `Dockerfile` to suit your app's build process
   * Update `k8s/deployment.yaml` with your app's ports, environment variables, etc.

5. **Open a Pull Request**
   Create a branch, push changes, and open a PR to `main`.
   The pipeline will handle the rest—build, test, scan, deploy to staging, and finally, to production.

---

## 🧪 Example Use Case

> Make a small change → Open a Pull Request → Automatically tested & deployed to staging → Merge → Deployed to production.

---

## 📌 Notes

* Minikube is used here for simplicity, making it ideal for local testing and learning. For production-scale systems, adapt the configuration for managed Kubernetes clusters (e.g., EKS, GKE, AKS).
* Ensure your self-hosted runner machine has adequate resources to run Minikube clusters and Docker builds efficiently.

---

## 💬 Questions or Contributions?

Feel free to open an issue or submit a pull request. Contributions are welcome!

---

Would you like this exported as a `README.md` file?


