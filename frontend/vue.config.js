const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  // publicPath: "http://0.0.0.0:8080/",
  publicPath: "/dist/static/",
  // publicPath: "https://nameless-fortress-82323.herokuapp.com/dist/",
  outputDir: "./dist/static/",

  chainWebpack: (config) => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);
    config.output.filename("bundle.js");
    config.optimization.splitChunks(false);
    config.resolve.alias.set("__STATIC__", "static");
    config.devServer
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },

  transpileDependencies: ["vuetify"],
};
