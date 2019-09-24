resource "aws_cloudwatch_log_group" "logs_api" {
  name              = "/aws/lambda/${local.lambda_api_fn_name}"
  retention_in_days = 14

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}
