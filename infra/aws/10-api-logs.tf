resource "aws_cloudwatch_log_group" "logs_api_excuse_list" {
  name              = "/aws/lambda/${local.lambda_api_excuse_list_fn_name}"
  retention_in_days = 14

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}

resource "aws_cloudwatch_log_group" "logs_api_excuse_add" {
  name              = "/aws/lambda/${local.lambda_api_excuse_add_fn_name}"
  retention_in_days = 14

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}
