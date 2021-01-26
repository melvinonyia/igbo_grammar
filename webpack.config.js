// work with all paths in a cross-platform manner
const path = require('path');

// plugins covered below
// configure source and distribution folder paths

// merge the common configuration with the environment specific configuration
module.exports = {
  context: __dirname,
  // entry point for application
  entry: './frontend/index.jsx',
  output: {
    path: path.resolve(__dirname, 'app', 'assets', 'javascripts'),
    filename: 'bundle.js'
  },
  module:{
    rules:[
      {
        // Specifies file types to transpile
        test: /\.js$|jsx/,
        // Leaves dependencies alone
        exclude: /node_modules/,
        // Sets Babel as the transpiler
        loader: 'babel-loader',
        options: {
          // Tells Babel what syntaxes to translate
          presets: ['@babel/env', '@babel/react']
        }
      }
    ]
  },
  devtool: 'source-map',

  resolve: {
    // Order matters, resolves left to right
    extensions: [".js", ".jsx", "*"]
  }
};
