function createElementFromTemplate(template) {
    return template.content.cloneNode(true).children[0];
}