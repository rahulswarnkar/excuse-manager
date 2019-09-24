resource "aws_dynamodb_table" "table_em" {
  name           = "${var.Application}-${var.Environment}-em"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "type"
  range_key      = "id"

  attribute {
    name = "type"
    type = "S"
  }

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}