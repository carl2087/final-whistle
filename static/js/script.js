document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // material boxed initialization
    let materialboxed = document.querySelectorAll('.materialboxed');
    M.Materialbox.init(materialboxed);

    // Modal initialization
    let elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});

// adds correct year to copyright in footer

$("#copyright").text(new Date().getFullYear());
