class URLStringParser {
    static parse(urlstring) {
        console.log('URLStringParser: ' + urlstring);

        var params = {};

        if (urlstring === '') return params;
        
        urlstring.split('&').forEach(item => {
            item = item.replace('?', '');
            var [name, value] = item.split('=');
            if (Object.keys(params).includes(name)) params[name].push(value);
            else params[name] = [value];
        });

        console.log(params);

        return params;
    }
}