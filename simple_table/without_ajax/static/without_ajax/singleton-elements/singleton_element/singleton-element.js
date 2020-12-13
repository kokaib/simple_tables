class SingletonElement extends Singleton {
    constructor(template) {
        super();
        this._template = template;
    }

    set template(value) {
        this._template = value;
    }

    createInstance() {
        return createElementFromTemplate(this._template);
    }

    appendInstance(elem) {
        if (this.instance.parentElement) this.instance.parentElement.removeChild(this.instance);
        this.instance.classList.remove('animatable');
        this.instance.classList.remove('removing');
        setTimeout(() => {this.instance.classList.add('animatable'); this.instance.classList.add('appending'); this.onAppendInstance(elem);}, 0);
    }

    onAppendInstance(elem) {
        const parent = elem ? elem : document.body;
        parent.appendChild(this.instance);
    }

    removeInstance() {
        this.instance.classList.remove('animatable');
        this.instance.classList.remove('appending');
        this.instance.addEventListener('animationend', this.onRemoveInstance, {once: true});
        setTimeout(() => {this.instance.classList.add('animatable'); this.instance.classList.add('removing');}, 0);
    }

    onRemoveInstance(ev) {
        ev.target.remove();
    }
}