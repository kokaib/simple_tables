class Singleton {
    constructor() {
        this._instance = null;
    }

    get instance() {
        if (!this._instance) this._instance = this.createInstance();
        return this._instance;
    }

    createInstance() {

    }
}