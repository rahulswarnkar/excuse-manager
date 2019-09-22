

resource "aws_lambda_function" "lambda_api" {
  filename      = "../../dist/fn.zip"
  function_name = "${local.lambda_api_fn_name}"
  role          = "${aws_iam_role.iam_role_api.arn}"
  handler       = "fn.handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${filebase64sha256("../../dist/fn.zip")}"

  runtime = "python3.7"

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}
