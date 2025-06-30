# List k8s images

Small utility to list all container images running in a Kubernetes cluster.

## Prerequisites

- Python 3.x
- `kubectl` configured
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/modcatz/k8s-list-images.git
cd k8s-list-images
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x list_k8s_images.py
```

## Usage

The script supports several options for filtering and displaying container images:

```bash
./list_k8s_images.py [options]
```

### Options

- `-n, --namespace`: Filter images by namespace
- `-l, --label`: Filter by label selector (e.g., app=nginx)
- `-u, --unique`: Show only unique images (removes duplicates)

### Examples

List all container images across all namespaces:
```bash
./list_k8s_images.py
```

List images in a specific namespace:
```bash
./list_k8s_images.py -n kube-system
```

List unique images only:
```bash
./list_k8s_images.py -u
```

List images with a specific label:
```bash
./list_k8s_images.py -l app=nginx
```

Combine filters:
```bash
./list_k8s_images.py -n default -l app=nginx -u
```

## Output

The script outputs a table with three columns:
- Namespace
- Pod name
- Image name

Example output:
```
Namespace    Pod                   Image
-----------  -------------------  ------------------------
kube-system  coredns-123abc      k8s.gcr.io/coredns:1.8
default      nginx-pod           nginx:1.19
```

## Troubleshooting

1. Make sure your kubeconfig is properly set up and you have access to the cluster:
```bash
kubectl cluster-info
```

2. If you get permission errors, ensure you have the necessary RBAC permissions to list pods across namespaces.
