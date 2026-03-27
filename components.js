/**
 * Toth Corretora - Shared Components
 * Custom Elements para Navbar e Footer reutilizáveis em todas as páginas.
 *
 * Uso:
 *   <toth-navbar active="sobre"></toth-navbar>
 *   <toth-footer></toth-footer>
 */

// =============================================
// TOTH NAVBAR COMPONENT
// =============================================
class TothNavbar extends HTMLElement {
  connectedCallback() {
    const active = this.getAttribute("active") || "home";
    // Resolve relative path prefix based on page depth
    const base = this.getAttribute("base") || "../../";

    const pages = {
      home: { href: `${base}pages/index.php/index.html`, label: "Home" },
      sobre: { href: `${base}pages/sobre.php/index.html`, label: "Sobre" },
      parceiros: {
        href: `${base}pages/parceiros.php/index.html`,
        label: "Parceiros",
      },
      contato: {
        href: `${base}pages/contato.php/index.html`,
        label: "Contato",
      },
    };

    const link = (key) => {
      const isActive = active === key;
      const cls = isActive
        ? "text-toth-gold font-semibold border-b-2 border-toth-gold pb-1"
        : "text-gray-600 hover:text-toth-dark font-medium transition-colors";
      return `<a href="${pages[key].href}" class="${cls}">${pages[key].label}</a>`;
    };

    this.innerHTML = `
        <!-- Top Bar -->
        <div class="bg-toth-dark text-white text-xs py-2.5 px-4">
            <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
                <div class="flex items-center flex-wrap gap-x-4 gap-y-1">
                    <a href="tel:4132055486" class="hover:text-toth-gold transition"><i class="fa fa-phone mr-1"></i>(41) 3205-5486</a>
                    <a href="https://wa.me/5541997127102" class="text-toth-gold font-medium hover:text-white transition"><i class="fa-brands fa-whatsapp mr-1"></i>(41) 99712-7102</a>
                    <a href="mailto:atendimento@tothcorretoradeseguros.com.br" class="hover:text-toth-gold transition"><i class="fa fa-envelope mr-1"></i>atendimento@tothcorretoradeseguros.com.br</a>
                </div>
                <div class="flex items-center gap-4 text-gray-400">
                    <span class="hidden sm:inline"><i class="fa fa-clock mr-1"></i>Seg à Sex - 8h às 18h</span>
                    <span class="hidden md:inline"><i class="fa fa-location-dot mr-1"></i>Curitiba, PR</span>
                    <div class="flex gap-3 text-white ml-1">
                        <a href="#" class="hover:text-toth-gold transition"><i class="fa-brands fa-facebook"></i></a>
                        <a href="#" class="hover:text-toth-gold transition"><i class="fa-brands fa-instagram"></i></a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Navbar -->
        <nav class="glass-nav sticky top-0 z-40 w-full shadow-sm">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between items-center h-20">
                    <a href="${pages.home.href}" class="flex-shrink-0">
                        <img class="h-14 w-auto" src="${base}images/logos/logo-horiz.png" alt="Toth Corretora">
                    </a>
                    <div class="hidden lg:flex items-center space-x-7">
                        ${link("home")}
                        ${link("sobre")}
                        <div class="relative group">
                            <button class="text-gray-600 hover:text-toth-dark font-medium transition flex items-center">
                                Seguros e mais <i class="fa fa-chevron-down text-[10px] ml-1.5 mt-0.5"></i>
                            </button>
                            <div class="absolute top-full left-0 w-60 bg-white shadow-2xl border border-gray-100 rounded-xl py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 translate-y-2 group-hover:translate-y-0">
                                <a href="${base}pages/seguro-de-pessoas.php/index.html" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-toth-gold transition">Seguros de Pessoas</a>
                                <a href="${base}pages/seguro-de-danos-patrimoniais.php/index.html" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-toth-gold transition">Danos / Patrimoniais</a>
                                <a href="${base}pages/responsabilidade-civil.php/index.html" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-toth-gold transition">Responsabilidade Civil</a>
                                <a href="${base}pages/consorcios.php/index.html" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-toth-gold transition">Consórcios</a>
                                <a href="${base}pages/planos-de-saude.php/index.html" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-toth-gold transition">Planos de Saúde</a>
                            </div>
                        </div>
                        ${link("parceiros")}
                        ${link("contato")}
                        <a href="https://wa.me/5541997127102" class="btn-gold text-white px-5 py-2.5 rounded-full font-medium text-sm shadow-lg flex items-center">
                            <i class="fa-brands fa-whatsapp mr-2 text-base"></i>Chamar no Whats
                        </a>
                    </div>
                    <!-- Mobile toggle -->
                    <button id="toth-menu-toggle" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-gray-100 transition">
                        <i class="fa fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
            <!-- Mobile Menu -->
            <div id="toth-mobile-menu" class="hidden lg:hidden border-t border-gray-100 bg-white px-4 pb-4">
                <div class="flex flex-col space-y-3 pt-4">
                    <a href="${pages.home.href}" class="text-gray-700 font-medium py-2 border-b border-gray-100">Home</a>
                    <a href="${pages.sobre.href}" class="text-gray-700 font-medium py-2 border-b border-gray-100">Sobre</a>
                    <a href="${base}pages/seguro-de-pessoas.php/index.html" class="text-gray-700 font-medium py-2 border-b border-gray-100">Seguros de Pessoas</a>
                    <a href="${base}pages/seguro-de-danos-patrimoniais.php/index.html" class="text-gray-700 font-medium py-2 border-b border-gray-100">Danos / Patrimoniais</a>
                    <a href="${base}pages/consorcios.php/index.html" class="text-gray-700 font-medium py-2 border-b border-gray-100">Consórcios</a>
                    <a href="${base}pages/planos-de-saude.php/index.html" class="text-gray-700 font-medium py-2 border-b border-gray-100">Planos de Saúde</a>
                    <a href="${pages.parceiros.href}" class="text-gray-700 font-medium py-2 border-b border-gray-100">Parceiros</a>
                    <a href="${pages.contato.href}" class="text-gray-700 font-medium py-2 border-b border-gray-100">Contato</a>
                    <a href="https://wa.me/5541997127102" class="btn-gold text-white px-5 py-3 rounded-full font-medium text-center">
                        <i class="fa-brands fa-whatsapp mr-2"></i>Chamar no WhatsApp
                    </a>
                </div>
            </div>
        </nav>`;

    const toggle = this.querySelector("#toth-menu-toggle");
    const menu = this.querySelector("#toth-mobile-menu");
    if (toggle && menu) {
      toggle.addEventListener("click", () => {
        menu.classList.toggle("hidden");
        const icon = toggle.querySelector("i");
        icon.classList.toggle("fa-bars");
        icon.classList.toggle("fa-xmark");
      });
    }
  }
}

// =============================================
// TOTH FOOTER COMPONENT
// =============================================
class TothFooter extends HTMLElement {
  connectedCallback() {
    const base = this.getAttribute("base") || "../../";
    const year = new Date().getFullYear();

    this.innerHTML = `
        <footer class="bg-toth-dark pt-14 pb-8">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-10">
                    <div class="col-span-1 md:col-span-2">
                        <img src="${base}images/logos/logo-horiz.png" alt="Toth Corretora" class="h-12 mb-5 brightness-0 invert opacity-90">
                        <p class="text-gray-400 text-sm leading-relaxed max-w-sm mb-5">
                            Soluções completas em seguros auto, vida, residencial e empresarial, com excelência no atendimento e as melhores seguradoras.
                        </p>
                        <div class="flex space-x-3">
                            <a href="#" class="footer-social w-9 h-9 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-all"><i class="fa-brands fa-facebook-f text-sm"></i></a>
                            <a href="#" class="footer-social w-9 h-9 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-all"><i class="fa-brands fa-instagram text-sm"></i></a>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-white font-bold uppercase tracking-wider mb-5 text-sm">Serviços</h4>
                        <ul class="space-y-2.5">
                            <li><a href="${base}pages/consorcios.php/index.html" class="text-gray-400 hover:text-toth-gold transition text-sm">Consórcios</a></li>
                            <li><a href="${base}pages/planos-de-saude.php/index.html" class="text-gray-400 hover:text-toth-gold transition text-sm">Planos de Saúde</a></li>
                            <li><a href="${base}pages/responsabilidade-civil.php/index.html" class="text-gray-400 hover:text-toth-gold transition text-sm">Responsabilidade Civil</a></li>
                            <li><a href="${base}pages/seguro-de-pessoas.php/index.html" class="text-gray-400 hover:text-toth-gold transition text-sm">Seguro de Pessoas</a></li>
                            <li><a href="${base}pages/seguro-de-danos-patrimoniais.php/index.html" class="text-gray-400 hover:text-toth-gold transition text-sm">Danos Patrimoniais</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-white font-bold uppercase tracking-wider mb-5 text-sm">Contato</h4>
                        <ul class="space-y-3">
                            <li class="flex items-start"><i class="fa fa-phone mt-1 text-toth-gold mr-3 text-xs"></i><span class="text-gray-400 text-sm">(41) 3205-5486<br>(41) 99712-7102</span></li>
                            <li class="flex items-start"><i class="fa fa-envelope mt-1 text-toth-gold mr-3 text-xs"></i><a href="mailto:atendimento@tothcorretoradeseguros.com.br" class="text-gray-400 hover:text-white transition text-sm break-all">atendimento@tothcorretoradeseguros.com.br</a></li>
                            <li class="flex items-start"><i class="fa fa-location-dot mt-1 text-toth-gold mr-3 text-xs"></i><span class="text-gray-400 text-sm">Curitiba, PR</span></li>
                        </ul>
                    </div>
                </div>
                <div class="pt-6 border-t border-white/10 text-center">
                    <p class="text-gray-500 text-xs">&copy; ${year} Toth Corretora de Seguros. Todos os direitos reservados.</p>
                </div>
            </div>
        </footer>`;
  }
}

// =============================================
// TOTH BASE STYLES (shared CSS classes)
// =============================================
const tothStyles = document.createElement("style");
tothStyles.textContent = `
.glass-nav { background: rgba(255,255,255,.97); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,0,0,.05); }
.btn-gold { background: linear-gradient(135deg,#c29b3a 0%,#b0892b 100%); transition: all .3s ease; }
.btn-gold:hover { box-shadow: 0 12px 24px -8px rgba(194,155,58,.6); transform: translateY(-2px); }
.text-gradient-gold { background: linear-gradient(135deg,#c29b3a,#d4b363); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.footer-social:hover { background: #c29b3a !important; border-color: transparent !important; color: white !important; }
`;
document.head.appendChild(tothStyles);

// Register custom elements
customElements.define("toth-navbar", TothNavbar);
customElements.define("toth-footer", TothFooter);
