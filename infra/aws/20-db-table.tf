resource "aws_dynamodb_table" "table_em" {
  name           = "${var.Application}-${var.Environment}-em"
  billing_mode   = "PAY_PER_REQUEST"
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