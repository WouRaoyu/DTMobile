const { VantResolver } = require("unplugin-vue-components/resolvers");
const ComponentsPlugin = require("unplugin-vue-components/webpack");
const path = require('path')
module.exports = {
    publicPath: '/',
    outputDir: 'dist',
    runtimeCompiler: true,
    devServer: {
        open: true,
        host: '0.0.0.0',
        port: 8080,
        https: false,
        hotOnly: false
    },
    configureWebpack: {
        module: {
            unknownContextCritical: false,
        },
        resolve: {
            alias: {
                '@': path.join(__dirname, "src")
            }
        },
        externals: {
            'Cesium': 'Cesium',
            'leaflet': 'leaflet'
        },
        plugins: [ComponentsPlugin({ resolvers: [VantResolver()] })]
    },
};