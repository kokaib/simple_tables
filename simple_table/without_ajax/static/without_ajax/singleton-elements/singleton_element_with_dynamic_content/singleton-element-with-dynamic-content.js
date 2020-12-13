class SingletonElementWithDynamicContent extends SingletonElement {
    set content(value) {
        this._content = value;
    }

    onAppendInstance(elem) {
        if (this._content) this.instance.querySelector('.content').appendChild(this._content);
        super.onAppendInstance(elem);
    }
}