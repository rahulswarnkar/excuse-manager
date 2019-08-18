module.exports = {
    entry: {
        'getState': './getState.js',
        'putState': './putState.js'
    },
    target: 'node',
    output: {
      path: `${__dirname}/dist`,
      filename: '[name].js',
      libraryTarget: 'umd'
    },
    resolve: {
        extensions: ['.ts', '.js'],
    }
  };