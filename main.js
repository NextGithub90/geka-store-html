/* =============================================
   GEKA STORE — main.js (Shared JavaScript)
   ============================================= */

(function () {

    // ---- NAVBAR SCROLL SHRINK ----
    var navbar = document.getElementById('main-navbar');
    var logo = document.getElementById('navbar-logo');

    function handleNavbarScroll() {
        if (!navbar || !logo) return;
        if (window.scrollY > 50) {
            navbar.classList.remove('h-24', 'bg-white/80');
            navbar.classList.add('h-16', 'bg-white/95', 'shadow-md');
            logo.classList.remove('h-12');
            logo.classList.add('h-8');
        } else {
            navbar.classList.remove('h-16', 'bg-white/95', 'shadow-md');
            navbar.classList.add('h-24', 'bg-white/80');
            logo.classList.remove('h-8');
            logo.classList.add('h-12');
        }
    }
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });

    // ---- MOBILE SIDEBAR ----
    var menuToggle = document.getElementById('menu-toggle');
    var menuClose = document.getElementById('menu-close');
    var sidebarMenu = document.getElementById('sidebar-menu');
    var sidebarBackdrop = document.getElementById('sidebar-backdrop');
    var sidebarPanel = document.getElementById('sidebar-panel');

    function openMenu() {
        if (!sidebarMenu) return;
        sidebarMenu.classList.remove('invisible');
        // Small delay so CSS transition fires after display
        setTimeout(function () {
            if (sidebarBackdrop) sidebarBackdrop.classList.remove('opacity-0');
            if (sidebarPanel) sidebarPanel.classList.remove('-translate-x-full');
        }, 10);
    }

    function closeMenu() {
        if (sidebarBackdrop) sidebarBackdrop.classList.add('opacity-0');
        if (sidebarPanel) sidebarPanel.classList.add('-translate-x-full');
        setTimeout(function () {
            if (sidebarMenu) sidebarMenu.classList.add('invisible');
        }, 300);
    }

    if (menuToggle) menuToggle.addEventListener('click', openMenu);
    if (menuClose) menuClose.addEventListener('click', closeMenu);
    if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeMenu);

})();
