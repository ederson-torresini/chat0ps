The configuration file `gcp.tf` is based on [Terraform container cluster documentation](https://www.terraform.io/docs/providers/google/r/container_cluster.html). The following steps are required to deploy the cluster in [GKE]((https://cloud.google.com/kubernetes-engine/)).

1. First, you need to create and download
[Google service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey).
Save as `gcp.json`.

2. Configure variables file `gcp.tfvars` using your own data: project and region/zone to deploy, and a username/password to login to K8s dashboard. Just a note: if you choose a region, GKE will create workers on ALL zones, multiplying by this factor the number of nodes.
```
gcp_project = "<insert your project here>"
gcp_zone = "<insert your zone here>"
gke_username = "<insert your GKE username here>"
gke_password = "<insert your GKE password here>"
```

3. Initialize working directory:
```bash
terraform init
```

4. Create the execution plan:
```bash
terraform plan -var-file=gcp.tfvars
```

5. Apply to achieve desired state (it takes about 1-2 min):
```bash
terraform apply -var-file=gcp.tfvars
```

6. Optionally, show up the current state:
```bash
terraform show
```
