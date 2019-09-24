resource "aws_api_gateway_rest_api" "rest_api" {
  name        = "${var.Application}-${var.Environment}-rest-api"
  description = "The API"

}

resource "aws_api_gateway_stage" "stage0" {
  stage_name    = "_"
  rest_api_id   = "${aws_api_gateway_rest_api.rest_api.id}"
  deployment_id = "${aws_api_gateway_deployment.rest_api_deployment.id}"

  tags = {
    application = "${var.Application}"
    environment = "${var.Environment}"
  }

}

resource "aws_api_gateway_deployment" "rest_api_deployment" {
  rest_api_id = "${aws_api_gateway_rest_api.rest_api.id}"

}