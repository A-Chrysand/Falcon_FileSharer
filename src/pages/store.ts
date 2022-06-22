function nginx_baseUrl(): string {
    const path_nginx_staitc = "/ignister/darkinfant/"
    if (process.env.NODE_ENV == 'production') {
        return path_nginx_staitc;
    } else {
        return '/';
    }
}

const login_url = "login"


export default {
    nginx_baseUrl, login_url
};