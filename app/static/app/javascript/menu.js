document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('open-btn');
    const closeBtn = document.getElementById('close-btn');

    // Abre o menu deslizando
    openBtn.onclick = () => {
        sidebar.style.left = '0';
    };

    // Fecha o menu escondendo
    closeBtn.onclick = () => {
        sidebar.style.left = '-100%';
    };
});