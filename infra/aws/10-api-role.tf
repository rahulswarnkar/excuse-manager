resource "aws_iam_role" "iam_role_api" {
  name = "api-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role        = "${aws_iam_role.iam_role_api.name}"
  policy_arn  = "${aws_iam_policy.lambda_logging.arn}"
}

resource "aws_iam_role_policy_attachment" "lambda_table" {
  role        = "${aws_iam_role.iam_role_api.name}"
  policy_arn  = "${aws_iam_policy.table_crud.arn}"
}