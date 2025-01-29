const webpack = require('webpack');

const config = {
    entry: __dirname + '/src/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
};

module.exports = config;