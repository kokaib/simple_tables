class SingletonElement extends Singleton {
    constructor(template) {
        super();

        this.isAppended = false;
        this.template = template;
    }

    set template(value) {
        this._template = value;
    }

    createInstance() {
        console.log('SingletonElement: createInstance');

        return createElementFromTemplate(this._template);
    }

    appendInstance(elem) {
        console.log('SingletonElement: appendInstance');

        this.isAppended = true;

        if (this.instance.parentElement) this.instance.parentElement.removeChild(this.instance);
        this.instance.classList.remove('animatable');
        this.instance.classList.remove('removing');
        setTimeout(() => {this.instance.classList.add('animatable'); this.instance.classList.add('appending'); this.onAppendInstance(elem);}, 0);
    }

    onAppendInstance(elem) {
        console.log('SingletonElement: onAppendInstance');

        const parent = elem ? elem : document.body;
        parent.appendChild(this.instance);
    }

    removeInstance() {
        console.log('SingletonElement: removeInstance');

        this.isAppended = false;

        this.instance.classList.remove('animatable');
        this.instance.classList.remove('appending');
        this.instance.addEventListener('animationend', this.onRemoveInstance, {once: true});
        setTimeout(() => {this.instance.classList.add('animatable'); this.instance.classList.add('removing');}, 0);
    }

    onRemoveInstance(ev) {
        console.log('SingletonElement: onRemoveInstance');

        ev.target.remove();
    }
}