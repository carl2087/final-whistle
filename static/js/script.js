document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});

// adds correct year to copyright in footer

$("#copyright").text(new Date().getFullYear());