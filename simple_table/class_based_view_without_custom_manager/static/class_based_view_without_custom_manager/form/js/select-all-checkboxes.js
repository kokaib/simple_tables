function selectAll(ev) {
    var form = ev.target.closest('input-field');
    var checkables = Array.from(
        form.querySelectorAll('input[type="checkbox"]')
    );
    checkables.forEach(item => {
        item.checked = true;
    });
}