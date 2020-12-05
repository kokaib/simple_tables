class Cookies {
    static getCookie(key) {
        const decodedCookies = decodeURIComponent(document.cookie);
        return decodedCookies.split('; ')
                .find(row => row.startsWith(key))
                .split('=')[1];
    }

    static setCookie(key) {

    }

    static removeCookie(key) {

    }
}