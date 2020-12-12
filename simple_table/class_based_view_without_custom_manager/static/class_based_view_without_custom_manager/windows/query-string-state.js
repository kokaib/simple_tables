class QueryStringState {

    constructor() {
        this._state = '';
    }

    set state(value) {
        console.log('QueryStringState: ' + value);
        this._state = value;
    }

    clearState() {
        this.state = '';
    }
    
    attachState(url) {
        console.log('attachState');
        
        if (this._state === '') return url;

        var [start, querystring] = url.includes('?') ? url.split('?') : [url, ''];

        console.log('start: ' + start);
        console.log('querystring: ' + querystring);

        var prevURL = URLStringParser.parse(this._state);
        var currURL = URLStringParser.parse(querystring);

        var end = '';
        for (var name of Object.keys(currURL)) {
            console.log('name: ' + name);
            if (Object.keys(prevURL).includes(name)) {
                delete prevURL[name]
            }
            for (var value of currURL[name]) {
                console.log('value: ' + value);
                end += '&' + name + '=' + value;
            }
        }

        console.log('end: ' + end);

        var middle = '';
        for (var name of Object.keys(prevURL)) {
            console.log('name: ' + name);
            for (var value of prevURL[name]) {
                console.log('value: ' + value);
                middle += (middle === '' ? '?' : '&') + name + '=' + value;
            }
        }

        console.log('middle: ' + middle);

        console.log('QueryStringState: ' + start + middle + end);

        return start + middle + end;
    }

}