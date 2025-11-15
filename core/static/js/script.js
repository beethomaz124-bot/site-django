const elementos = document.querySelectorAll(".scroll-animation");

function animarScroll() {
    const alturaJanela = window.innerHeight;

    elementos.forEach(el => {
        const posicao = el.getBoundingClientRect().top;
        if (posicao < alturaJanela - 100) {
            el.classList.add("show");
        } else {
            el.classList.remove("show");
        }
    });
}

window.addEventListener("scroll", animarScroll);
window.addEventListener("load", animarScroll);

document.addEventListener("DOMContentLoaded", () => {
    const menuHamburguer = document.getElementById('menu-hamburguer');
    const navegacao = document.getElementById('navegacao');
    const links = document.querySelectorAll('.navegacao a');

    menuHamburguer.addEventListener('click', (e) => {
        e.stopPropagation();
        navegacao.classList.toggle('active');
    });

    links.forEach(link => {
        link.addEventListener('click', () => {
            navegacao.classList.remove('active');
        });
    });

    document.addEventListener('click', (e) => {
        if (!navegacao.contains(e.target) && !menuHamburguer.contains(e.target)) {
            navegacao.classList.remove('active');
        }
    });
});

