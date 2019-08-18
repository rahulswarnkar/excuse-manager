module.exports = (event, context, callback) => {
    // See https://thecodebarbarian.com/bundling-a-node-js-function-for-aws-lambda-with-webpack
    context.callbackWaitsForEmptyEventLoop = false;
  
    fn().
      then(res => {
        callback(null, {
          statusCode: 200,
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true
          },
          body: JSON.stringify(res)
        });
        console.log('done');
      }).
      catch(error => callback(error));
  };