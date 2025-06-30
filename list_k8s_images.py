#!/usr/bin/env python3
import argparse
from kubernetes import client, config
from tabulate import tabulate

def get_images(namespace=None, label_selector=None, deduplicate=False):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    images = []
    pods = v1.list_pod_for_all_namespaces(label_selector=label_selector) if not namespace else v1.list_namespaced_pod(namespace, label_selector=label_selector)
    for pod in pods.items:
        ns = pod.metadata.namespace
        pod_name = pod.metadata.name
        for container in pod.spec.containers:
            images.append((ns, pod_name, container.image))
    return images

def main():
    parser = argparse.ArgumentParser(description="List all container images running in a Kubernetes cluster.")
    parser.add_argument('-n','--namespace', help='Filter by namespace')
    parser.add_argument('-l','--label', help='Filter by label selector (e.g. app=nginx)')
    parser.add_argument('-u','--unique', action='store_true', help='Avoid listing duplicate images')
    args = parser.parse_args()

    images = get_images(namespace=args.namespace, label_selector=args.label)
    table_data = []
    seen = set()

    for ns, pod, image in images:
        key = (image,) if args.unique else (ns, pod, image)
        if args.unique and key in seen:
            continue
        seen.add(key)
        table_data.append([ns, pod, image])

    headers = ["Namespace", "Pod", "Image"]
    print(tabulate(table_data, headers=headers, tablefmt="simple"))

if __name__ == "__main__":
    main() 