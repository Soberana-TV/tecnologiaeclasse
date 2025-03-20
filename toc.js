// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="o_que.html"><strong aria-hidden="true">1.</strong> O que é Tecnologia e Classe?</a></li><li class="chapter-item expanded "><a href="rustlings_pt1.html"><strong aria-hidden="true">2.</strong> Vamos aprender Rust pt. 1</a></li><li class="chapter-item expanded "><a href="mozilla_firefox.html"><strong aria-hidden="true">3.</strong> Os Termos de Uso do Firefox</a></li><li class="chapter-item expanded "><a href="rust_linux.html"><strong aria-hidden="true">4.</strong> Rust no Linux</a></li><li class="chapter-item expanded "><a href="13_03_25.html"><strong aria-hidden="true">5.</strong> 13/03/25</a></li><li class="chapter-item expanded "><a href="06_03_25.html"><strong aria-hidden="true">6.</strong> 06/03/25</a></li><li class="chapter-item expanded "><a href="27_02_25.html"><strong aria-hidden="true">7.</strong> 27/02/25</a></li><li class="chapter-item expanded "><a href="ia_nos_deixa_burros.html"><strong aria-hidden="true">8.</strong> A IA nos deixa burros?</a></li><li class="chapter-item expanded "><a href="futuro_do_trabalho.html"><strong aria-hidden="true">9.</strong> O futuro do trabalho?</a></li><li class="chapter-item expanded "><a href="amazon_kindle.html"><strong aria-hidden="true">10.</strong> Baixe seus livros da Amazon</a></li><li class="chapter-item expanded "><a href="worldcoin.html"><strong aria-hidden="true">11.</strong> Sobre a Worldcoin de Sam Altman</a></li><li class="chapter-item expanded "><a href="ollama_deepseek.html"><strong aria-hidden="true">12.</strong> Tutorial Ollama e Deepseek</a></li><li class="chapter-item expanded "><a href="milei_libra.html"><strong aria-hidden="true">13.</strong> O golpe de cripto do Milei</a></li><li class="chapter-item expanded "><a href="doge_hackeado.html"><strong aria-hidden="true">14.</strong> DOGE de Musk é hackeado</a></li><li class="chapter-item expanded "><a href="preservacao_digital.html"><strong aria-hidden="true">15.</strong> Sobre a preservação digital</a></li><li class="chapter-item expanded "><a href="meta_pirateou.html"><strong aria-hidden="true">16.</strong> META pirateou 81TB de livros</a></li><li class="chapter-item expanded "><a href="06_02_25.html"><strong aria-hidden="true">17.</strong> 06/02/25</a></li><li class="chapter-item expanded "><a href="30_01_25.html"><strong aria-hidden="true">18.</strong> 30/01/25</a></li><li class="chapter-item expanded "><a href="deepseek.html"><strong aria-hidden="true">19.</strong> Deepseek abala os EUA</a></li><li class="chapter-item expanded "><a href="descentralizadas.html"><strong aria-hidden="true">20.</strong> Redes sociais descentralizadas</a></li><li class="chapter-item expanded "><a href="23_01_25.html"><strong aria-hidden="true">21.</strong> 23/01/25</a></li><li class="chapter-item expanded "><a href="16_01_25.html"><strong aria-hidden="true">22.</strong> 16/01/25</a></li><li class="chapter-item expanded "><a href="09_01_25.html"><strong aria-hidden="true">23.</strong> 09/01/25</a></li><li class="chapter-item expanded "><a href="honey.html"><strong aria-hidden="true">24.</strong> Como a Honey roubou todo mundo</a></li><li class="chapter-item expanded "><a href="golpes_email.html"><strong aria-hidden="true">25.</strong> Investigando Golpes de e-mail</a></li><li class="chapter-item expanded "><a href="musica2024.html"><strong aria-hidden="true">26.</strong> Especial Música de 2024</a></li><li class="chapter-item expanded "><a href="19_12_24.html"><strong aria-hidden="true">27.</strong> 19/12/24</a></li><li class="chapter-item expanded "><a href="ia_do_inss.html"><strong aria-hidden="true">28.</strong> IA do INSS</a></li><li class="chapter-item expanded "><a href="12_12_24.html"><strong aria-hidden="true">29.</strong> 12/12/24</a></li><li class="chapter-item expanded "><a href="05_12_24.html"><strong aria-hidden="true">30.</strong> 05/12/24</a></li><li class="chapter-item expanded "><a href="28_11_24.html"><strong aria-hidden="true">31.</strong> 28/11/24</a></li><li class="chapter-item expanded "><a href="25_11_24.html"><strong aria-hidden="true">32.</strong> 25/11/24</a></li><li class="chapter-item expanded "><a href="aeria.html"><strong aria-hidden="true">33.</strong> Projeto com Aeria</a></li><li class="chapter-item expanded "><a href="14_11_24.html"><strong aria-hidden="true">34.</strong> 14/11/24</a></li><li class="chapter-item expanded "><a href="07_11_24.html"><strong aria-hidden="true">35.</strong> 07/11/24</a></li><li class="chapter-item expanded "><a href="31_10_24.html"><strong aria-hidden="true">36.</strong> 31/10/24</a></li><li class="chapter-item expanded "><a href="fetiche_tecnologia2.html"><strong aria-hidden="true">37.</strong> Fetiche da Tecnologia 2</a></li><li class="chapter-item expanded "><a href="wordpress.html"><strong aria-hidden="true">38.</strong> Wordpress VS WP Engine</a></li><li class="chapter-item expanded "><a href="24_10_24.html"><strong aria-hidden="true">39.</strong> 24/10/24</a></li><li class="chapter-item expanded "><a href="17_10_24.html"><strong aria-hidden="true">40.</strong> 17/10/24</a></li><li class="chapter-item expanded "><a href="10_10_24.html"><strong aria-hidden="true">41.</strong> 10/10/24</a></li><li class="chapter-item expanded "><a href="godot.html"><strong aria-hidden="true">42.</strong> O Fork da Godot</a></li><li class="chapter-item expanded "><a href="07_10_24.html"><strong aria-hidden="true">43.</strong> 07/10/24</a></li><li class="chapter-item expanded "><a href="28_09_24.html"><strong aria-hidden="true">44.</strong> 28/09/24</a></li><li class="chapter-item expanded "><a href="19_09_24.html"><strong aria-hidden="true">45.</strong> 19/09/24</a></li><li class="chapter-item expanded "><a href="16_09_24.html"><strong aria-hidden="true">46.</strong> 16/09/24</a></li><li class="chapter-item expanded "><a href="05_09_24.html"><strong aria-hidden="true">47.</strong> 05/09/24</a></li><li class="chapter-item expanded "><a href="29_08_24.html"><strong aria-hidden="true">48.</strong> 29/08/24</a></li><li class="chapter-item expanded "><a href="22_08_24.html"><strong aria-hidden="true">49.</strong> 22/08/24</a></li><li class="chapter-item expanded "><a href="15_08_24.html"><strong aria-hidden="true">50.</strong> 15/08/24</a></li><li class="chapter-item expanded "><a href="cookie_clicker.html"><strong aria-hidden="true">51.</strong> Cookie Clicker</a></li><li class="chapter-item expanded "><a href="08_08_24.html"><strong aria-hidden="true">52.</strong> 08/08/24</a></li><li class="chapter-item expanded "><a href="01_08_24.html"><strong aria-hidden="true">53.</strong> 01/08/24</a></li><li class="chapter-item expanded "><a href="25_07_24.html"><strong aria-hidden="true">54.</strong> 25/07/24</a></li><li class="chapter-item expanded "><a href="apagao.html"><strong aria-hidden="true">55.</strong> Crowdstrike / Apagão Cibernético</a></li><li class="chapter-item expanded "><a href="18_07_24.html"><strong aria-hidden="true">56.</strong> 18/07/24</a></li><li class="chapter-item expanded "><a href="11_07_24.html"><strong aria-hidden="true">57.</strong> 11/07/24</a></li><li class="chapter-item expanded "><a href="04_07_24.html"><strong aria-hidden="true">58.</strong> 04/07/24</a></li><li class="chapter-item expanded "><a href="27_06_24.html"><strong aria-hidden="true">59.</strong> 27/06/24</a></li><li class="chapter-item expanded "><a href="20_06_24.html"><strong aria-hidden="true">60.</strong> 20/06/24</a></li><li class="chapter-item expanded "><a href="comunistas_internet.html"><strong aria-hidden="true">61.</strong> Comunistas na Internet</a></li><li class="chapter-item expanded "><a href="13_06_24.html"><strong aria-hidden="true">62.</strong> 13/06/24</a></li><li class="chapter-item expanded "><a href="06_06_24.html"><strong aria-hidden="true">63.</strong> 06/06/24</a></li><li class="chapter-item expanded "><a href="extrema_direita_ti.html"><strong aria-hidden="true">64.</strong> A Ideologia de Extrema Direita na TI</a></li><li class="chapter-item expanded "><a href="30_05_24.html"><strong aria-hidden="true">65.</strong> 30/05/24</a></li><li class="chapter-item expanded "><a href="23_05_24.html"><strong aria-hidden="true">66.</strong> 23/05/24</a></li><li class="chapter-item expanded "><a href="09_05_24.html"><strong aria-hidden="true">67.</strong> 09/05/24</a></li><li class="chapter-item expanded "><a href="02_05_24.html"><strong aria-hidden="true">68.</strong> 02/05/24</a></li><li class="chapter-item expanded "><a href="30_04_24.html"><strong aria-hidden="true">69.</strong> 30/04/24</a></li><li class="chapter-item expanded "><a href="18_04_24.html"><strong aria-hidden="true">70.</strong> 18/04/24</a></li><li class="chapter-item expanded "><a href="11_04_24.html"><strong aria-hidden="true">71.</strong> 11/04/24</a></li><li class="chapter-item expanded "><a href="04_04_24.html"><strong aria-hidden="true">72.</strong> 04/04/24</a></li><li class="chapter-item expanded "><a href="ideologia_californiana.html"><strong aria-hidden="true">73.</strong> A Ideologia Californiana</a></li><li class="chapter-item expanded "><a href="anticheat.html"><strong aria-hidden="true">74.</strong> Vanguard, LoL e Anticheat</a></li><li class="chapter-item expanded "><a href="28_03_24.html"><strong aria-hidden="true">75.</strong> 28/03/24</a></li><li class="chapter-item expanded "><a href="25_03_24.html"><strong aria-hidden="true">76.</strong> 25/03/24</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
