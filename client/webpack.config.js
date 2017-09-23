/* eslint-disable */
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const STAGE = process.env.NODE_ENV || 'DEVELOPMENT';

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve('./dist'),
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
    ],
    rules: [
      {
        test: /\.css$/,
        // the order in which webpack applies loaders on the matching resources is from last to first
        use: ExtractTextPlugin.extract({ 
          fallback:'style-loader',
          use:['css-loader'],
        })
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['env', 'react']
          }
        }
      }
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: "Lego Collector's Tools",
      showErrors: STAGE === 'DEVELOPMENT'
    }),
    new ExtractTextPlugin({filename:'bundle.css'}),
  ],
  watchOptions: {
    poll: true
  }
}