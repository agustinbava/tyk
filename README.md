# Deployment Monitor

This repository contains a Helm chart for deploying a Python script as a Kubernetes Deployment in a Kubernetes cluster. The Python script monitors deployments in the cluster and performs health checks.

## Prerequisites

Before deploying the Python script using this Helm chart, ensure that you have the following prerequisites installed:

- Kubernetes cluster (e.g., Minikube)
- Helm (Helm 3 recommended)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
   ```
2. Change into the deployment-monitor directory:
    ```bash
        cd deployment-monitor
    ```
3. Install Helm chart
    ```bash
        helm install <release_name> deployment-monitor -n <namespace>
    ```

# Usage
Once the Helm chart is installed, the Python script will be deployed as a Kubernetes Deployment in the cluster. It will monitor the deployments in the cluster and perform health checks.

# Uninstallation
To uninstall the Helm chart and remove the deployed resources from the cluster, use the following command:
    ```bash
    helm uninstall <release_name>
    ```

# Output example
```
agustingimenezbava@Agustins-MBP-2 ~ % kubectl logs my-deployment-monitor-deployment-55bf6d87dc-669q5 -n monitor
INFO:root:2024-04-20 01:16:17: INFO= Heartbeat OK.
INFO:root:2024-04-20 01:16:17: INFO= Deployment dummylogger in namespace dummy-logger is healthy.
INFO:root:2024-04-20 01:16:17: INFO= Deployment coredns in namespace kube-system is healthy.
INFO:root:2024-04-20 01:16:17: INFO= Deployment deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:17: INFO= Deployment kps-grafana in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:17: INFO= Deployment kps-kube-prometheus-stack-operator in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:17: INFO= Deployment kps-kube-state-metrics in namespace monitor is healthy.
ERROR:root:2024-04-20 01:16:17: ERROR= Deployment my-deployment-monitor-deployment in namespace monitor is unhealthy: None/1 replicas ready.
INFO:root:2024-04-20 01:16:27: INFO= Heartbeat OK.
INFO:root:2024-04-20 01:16:27: INFO= Deployment dummylogger in namespace dummy-logger is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment coredns in namespace kube-system is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment kps-grafana in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment kps-kube-prometheus-stack-operator in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment kps-kube-state-metrics in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:27: INFO= Deployment my-deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Heartbeat OK.
INFO:root:2024-04-20 01:16:37: INFO= Deployment dummylogger in namespace dummy-logger is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment coredns in namespace kube-system is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment kps-grafana in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment kps-kube-prometheus-stack-operator in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment kps-kube-state-metrics in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:37: INFO= Deployment my-deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Heartbeat OK.
INFO:root:2024-04-20 01:16:47: INFO= Deployment dummylogger in namespace dummy-logger is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment coredns in namespace kube-system is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment kps-grafana in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment kps-kube-prometheus-stack-operator in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment kps-kube-state-metrics in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:47: INFO= Deployment my-deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Heartbeat OK.
INFO:root:2024-04-20 01:16:57: INFO= Deployment dummylogger in namespace dummy-logger is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment coredns in namespace kube-system is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment deployment-monitor-deployment in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment kps-grafana in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment kps-kube-prometheus-stack-operator in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment kps-kube-state-metrics in namespace monitor is healthy.
INFO:root:2024-04-20 01:16:57: INFO= Deployment my-deployment-monitor-deployment in namespace monitor is healthy.
```
