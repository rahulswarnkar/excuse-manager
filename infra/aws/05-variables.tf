variable "AccountId" {
  description = "AWS Account ID"
  type        = "string"
}

variable "Region" {
  description = "AWS region"
  type        = "string"
}

variable "Application" {
  description = "The name of the application to tag all resources."
  type        = "string"
}

variable "Environment" {
  description = "The environment/workspace being executed."
  type        = "string"
}