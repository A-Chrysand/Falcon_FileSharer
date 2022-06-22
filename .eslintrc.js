module.exports = {
	root: true,
	env: {
		node: true
	},
	'extends': [
		'plugin:vue/vue3-essential',
		'eslint:recommended',
		'@vue/typescript/recommended'
	],
	parserOptions: {
		ecmaVersion: 2020
	},
	rules: {
		//语法检查
		'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'no-tabs': 0,                   //禁止tab缩进
		'no-mixed-spaces-and-tabs': 0,  //禁止space和tab混用
		'indent': ["off", "tab"],       //缩进使用tabl
		'no-trailing-spaces': 0,        //禁止结尾空格
	}
}
