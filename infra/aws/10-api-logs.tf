resource "aws_cloudwatch_log_group" "logs_api" {
  name              = "/aws/lambda/${local.lambda_api_fn_name}"
  retention_in_days = 14

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role = "${aws_iam_role.iam_role_api.name}"
  policy_arn = "${aws_iam_policy.lambda_logging.arn}"
}
