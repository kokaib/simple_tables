class WindowDispatcher {

    constructor(switchboard) {
        if (switchboard) this._switchboard = switchboard;
    }

    get switchboard() {
        return this._switchboard;
    }

    set switchboard(value) {
        this._switchboard = value;
    }

    onResponseAvailable(responseText) {
        var response = JSON.parse(responseText);

        var id = response['id'];
        // can't use this if it's called from a fetch promise...
        // TODO: return instances of this class from a static method (?)
        var handler = windowDispatcher._switchboard[id];
        var data = response['data'];

        handler(data);
    }

    onResponseFailed(response) {
        console.log(response);
    }

}