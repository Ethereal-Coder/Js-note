var webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
path = require('path');

module.exports = {
    entry: {
        //add [] to fix: Module not found: Error: a dependency to an entry point is not allowed
        './amazeui-1.0.0': ['./src/amazeui'],
        './index': ['./src/index']
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'dist')
    },
    module:{
        loaders:[
            {
                test: /\.(js|jsx)$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                loader: 'style-loader!css-loader!sass-loader'
            },
            {
                test: /\.svg|woff|eot|ttf$/,
                loader: require.resolve('file-loader') + '?name=[path][name].[ext]'
            }
        ]
    },
    resolve:{
        extensions:['.js','.jsx']
    }
}
;

