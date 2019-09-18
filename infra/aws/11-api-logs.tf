resource "aws_cloudwatch_log_group" "logs_api" {
  name              = "/excuse-manager/api/${aws_iam_role.iam_role_api.name}"
  retention_in_days = 14
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role = "${aws_iam_role.iam_role_api.name}"
  policy_arn = "${aws_iam_policy.lambda_logging.arn}"
}
