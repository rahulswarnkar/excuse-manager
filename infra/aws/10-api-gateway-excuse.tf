resource "aws_api_gateway_resource" "rest_api_excuse_resource" {
  rest_api_id = "${aws_api_gateway_rest_api.rest_api.id}"
  parent_id   = "${aws_api_gateway_rest_api.rest_api.root_resource_id}"
  path_part   = "excuse"
}

resource "aws_api_gateway_method" "rest_api_excuse_method_get" {
  rest_api_id   = "${aws_api_gateway_rest_api.rest_api.id}"
  resource_id   = "${aws_api_gateway_resource.rest_api_excuse_resource.id}"
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "rest_api_excuse_integration" {
  rest_api_id             = "${aws_api_gateway_rest_api.rest_api.id}"
  resource_id             = "${aws_api_gateway_resource.rest_api_excuse_resource.id}"
  http_method             = "${aws_api_gateway_method.rest_api_excuse_method_get.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "arn:aws:apigateway:${var.Region}:lambda:path/2015-03-31/functions/${aws_lambda_function.lambda_api.arn}/invocations"
}

resource "aws_lambda_permission" "rest_api_lambda_permission" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.lambda_api.function_name}"
  principal     = "apigateway.amazonaws.com"

  source_arn = "arn:aws:execute-api:${var.Region}:${var.AccountId}:${aws_api_gateway_rest_api.rest_api.id}/*/${aws_api_gateway_method.rest_api_excuse_method_get.http_method}${aws_api_gateway_resource.rest_api_excuse_resource.path}"
}

