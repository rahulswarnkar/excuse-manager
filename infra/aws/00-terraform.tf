terraform {
  backend "s3" {
    bucket = "excuse-manager-tf-state"
    key    = "dev.tfstate"
    region = "eu-west-1"
  }
}
