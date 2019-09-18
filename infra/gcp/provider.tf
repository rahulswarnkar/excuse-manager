provider "google" {
    version = "2.14"
    project = "excuse-manager"
    region  = "europe-west1"
    zone    = "europe-west1-c"
}

terraform {
    backend "gcs" {
        bucket = "tf-infra-state-20190917"
        prefix  = "dev"
    }
}
