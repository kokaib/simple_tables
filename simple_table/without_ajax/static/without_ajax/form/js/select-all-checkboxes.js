function selectAll(ev, selector) {
    Array.from(
        ev.target.closest(selector).querySelectorAll('input[type="checkbox"]')
    )
    .forEach(item => {
        item.checked = true;
    });
}