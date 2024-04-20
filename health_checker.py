from kubernetes import client, config
import yaml
import logging
import time
from datetime import datetime

# logging.basicConfig(filename="hc.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO)

def heartbeat():
    try:
        # Load kube config
        # config.load_kube_config()
        config.load_incluster_config()
        
        # Create a CoreV1Api client instance
        v1 = client.CoreV1Api()
        
        # Attempt to list namespaces as a test of API server connectivity
        v1.list_namespace()

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: INFO= Heartbeat OK.")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: INFO= Heartbeat OK.")
        return True
    except Exception as e:
        # If the call fails, print a failure message
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: ERROR= Heartbeat failed: {str(e)}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: ERROR= Heartbeat failed: {str(e)}")
        return False
    
def monitor_deployments():
    # Load the kubeconfig file from the default location (e.g., ~/.kube/config)
    # config.load_kube_config()

    # For in-cluster configuration use:
    config.load_incluster_config()

    # Create a v1 Core API client object
    # v1 = client.CoreV1Api()

    # Create a App v1 Core API client object 
    v1 = client.AppsV1Api()

    while True:
        print("Checking deployments...")

        # List all deployments across all namespaces
        deployments = v1.list_deployment_for_all_namespaces()
        
        for deploy in deployments.items:
            desired_replicas = deploy.spec.replicas
            current_replicas = deploy.status.ready_replicas

            # Check if the deployment has the desired number of replicas
            if current_replicas == desired_replicas or (current_replicas == None and desired_replicas == 0):
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: INFO= Deployment {deploy.metadata.name} in namespace {deploy.metadata.namespace} is healthy.")
                logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: INFO= Deployment {deploy.metadata.name} in namespace {deploy.metadata.namespace} is healthy.")
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: ERROR= Deployment {deploy.metadata.name} in namespace {deploy.metadata.namespace} is unhealthy: "
                      f"{current_replicas}/{desired_replicas} replicas ready.")
                logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: ERROR= Deployment {deploy.metadata.name} in namespace {deploy.metadata.namespace} is unhealthy: "
                      f"{current_replicas}/{desired_replicas} replicas ready.")
        
        time.sleep(10)
        heartbeat()

if '__main__' == __name__:
    while True:
        if heartbeat():
            monitor_deployments()
        time.sleep(60)