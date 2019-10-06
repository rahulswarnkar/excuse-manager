resource "aws_lambda_function" "lambda_api_excuse_list" {
  filename      = "../../dist/fn.zip"
  function_name = "${local.lambda_api_excuse_list_fn_name}"
  role          = "${aws_iam_role.iam_role_api.arn}"
  handler       = "fn.list"

  source_code_hash = "${filebase64sha256("../../dist/fn.zip")}"

  runtime = "python3.7"

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}

resource "aws_lambda_function" "lambda_api_excuse_add" {
  filename      = "../../dist/fn.zip"
  function_name = "${local.lambda_api_excuse_add_fn_name}"
  role          = "${aws_iam_role.iam_role_api.arn}"
  handler       = "fn.add"

  source_code_hash = "${filebase64sha256("../../dist/fn.zip")}"

  runtime = "python3.7"

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }
}
