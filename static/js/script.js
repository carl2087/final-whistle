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

// times out the message alerts

    setTimeout(function () {
        $('#message-alert').fadeOut('fast');
    },2000)
});

// adds correct year to copyright in footer

$("#copyright").text(new Date().getFullYear());
