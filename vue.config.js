module.exports = {
	publicPath: './',			//输出文件目录
	assetsDir: './',
	outputDir: 'darkinfant',
	devServer: {
		port: 8080,
		proxy: {
			'/jsGet': {
				//目标服务器,代理访问到http://localhost:8888
				target: "http://localhost:8000",
				changOrigin: true, //开启代理

			},
			'/jsPost': {
				target: "http://localhost:8000",
				changOrigin: true, //开启代理
			},

			'/jsStream': {
				target: "http://localhost:8000",
				changOrigin: true, //开启代理
				pathRewrite: {
					'^/jsStream': '/jsStream'
				}
			},
			'/share': {
				target: "http://localhost:8000",
				changOrigin: true, //开启代理
			}
		},
	},
	pages: {
		index: {
			entry: "src/pages/home/main.ts",
			template: "public/index.html",
			filename: "index.html",
			title: "index"
		},
		login: {
			entry: "src/pages/login/login.ts",
			template: "public/index.html",
			filename: "login.html",
			title: "login",
		}
	},/*
	chainWebpack: (config) => {
		if (process.env.NODE_ENV === 'production') {
			config.plugin('html').tap((opts) => {
				opts[0].filename = './index.html';
				//  ./是以dist为根目录开始的
				return opts;
			});
		}

	},*/

};