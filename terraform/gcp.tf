// Variables
variable "gcp_project" { }
variable "gcp_zone" { }
variable "gke_username" { }
variable "gke_password" { }


// Provider
// https://www.terraform.io/docs/providers/google/index.html
provider "google" {
  // https://console.cloud.google.com/apis/credentials/serviceaccountkey
  credentials = "${file("gcp.json")}"
  project = "${var.gcp_project}"
  zone = "${var.gcp_zone}"
}


// Resources
// https://www.terraform.io/docs/providers/google/r/container_cluster.html
resource "google_container_cluster" "chatops" {
  name = "chatops"

  master_auth {
    username = "${var.gke_username}"
    password = "${var.gke_password}"
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
