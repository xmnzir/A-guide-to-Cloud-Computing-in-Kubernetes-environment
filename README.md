# A Guide to Cloud Computing in Kubernetes Environment

## 📖 Project Overview

This project demonstrates how to deploy, monitor, and benchmark applications in a Kubernetes environment.

It covers:

🚀 Kubernetes Dashboard Deployment

📦 JavaBenchmarkApp Deployment

📊 Monitoring Stack Setup (Prometheus + Grafana)

⚡ Load Generator Implementation

🔍 Application Benchmarking

⚙️ Technologies Used

🐳 Docker – Containerization of Load Generator

☸️ Kubernetes – Container orchestration

📦 Helm – Kubernetes package manager

📡 Prometheus – Metrics collection

📈 Grafana – Monitoring & visualization

🐍 Python – Custom load generator script



## Key Components
✅ Task 1: Kubernetes Dashboard & JavaBenchmarkApp

Deployed Kubernetes Dashboard with Helm.

Created ServiceAccount with admin privileges.

Deployed and exposed JavaBenchmarkApp on NodePort 30000.

✅ Task 2: Monitoring Stack (Prometheus + Grafana)

Installed Prometheus & Grafana via Helm.

Exposed services for local access.

Configured Prometheus as Grafana’s data source.

✅ Task 3: Load Generator

Python-based tool using requests + threading.

Environment-configurable:

TARGET → App endpoint

FREQUENCY → Request rate

Packaged as a Docker image for reusability.

✅ Task 4: Benchmarking

Deployed the Load Generator in Kubernetes.



## Results

📈 CPU & Memory usage increased with higher request load.

⚠️ Peak loads → spikes in resource utilization.

❌ Failed requests reduced load → resource usage dropped.

👀 Grafana dashboards enabled real-time monitoring & insights.



## 📌 Conclusion

This coursework showcases how to:
✔️ Deploy and manage applications in Kubernetes.
✔️ Set up a Prometheus + Grafana monitoring stack.
✔️ Implement and containerize a Python-based load generator.
✔️ Benchmark and analyze resource usage under varying load.



👉 By combining monitoring + benchmarking, the project enables better performance optimization and capacity planning in cloud environments.
