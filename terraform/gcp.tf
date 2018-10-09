// Provider
// https://www.terraform.io/docs/providers/google/index.html
provider "google" {
  // https://console.cloud.google.com/apis/credentials/serviceaccountkey
  credentials = "${file("gcp.json")}"
  project = "<insert your project here>"
  region = "<insert your region here>"
}


// Resources
// https://www.terraform.io/docs/providers/google/r/container_cluster.html
resource "google_container_cluster" "chatops" {
  name = "chatops"

  master_auth {
    username = "<insert your username here>"
    password = "<insert you password here>"
  }
}


// Outputs
output "master_endpoint" {
  value = "${google_container_cluster.chatops.endpoint}"
}

output "client_certificate" {
  value = "${google_container_cluster.chatops.master_auth.0.client_certificate}"
}

output "client_key" {
  value = "${google_container_cluster.chatops.master_auth.0.client_key}"
}

output "cluster_ca_certificate" {
  value = "${google_container_cluster.chatops.master_auth.0.cluster_ca_certificate}"
}
