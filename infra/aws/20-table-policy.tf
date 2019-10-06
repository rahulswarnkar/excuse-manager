resource "aws_iam_policy" "table_crud" {
  name        = "${var.Application}-${var.Environment}-dynamodb-table-crud"
  path        = "/"
  description = "Policy for CRUD operations on dynamodb table"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "dynamodb:Query",
        "dynamodb:PutItem"
      ],
      "Effect": "Allow",
      "Resource": "${aws_dynamodb_table.table_em.arn}"
    }
  ]
}
EOF
}