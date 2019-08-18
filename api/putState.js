const handler = require('./handler');

exports.handler = handler(getState);

async function getState() {
  return {};
}