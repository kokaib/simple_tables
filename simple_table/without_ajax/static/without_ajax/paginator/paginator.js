function pageTo(n) {
    var startingURL = window.location.href;
    startingURL = startingURL.replace(/&page=\d+/g, '');
    window.location.href = `${startingURL}${startingURL.includes('?') ? startingURL.endsWith('?') ? '' : '&' : '?'}page=${n}`;
}