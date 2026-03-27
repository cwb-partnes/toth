import re
import os

filepath = r"c:\projetos\landing_page\site-toth-clonado\site\pages\index.php\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir o GRID por TABS
new_services = """    <!-- ===== SERVICES TABS ===== -->
    <section id="services" class="py-20 bg-toth-light relative -mt-8 z-30">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-3xl md:text-4xl font-extrabold text-toth-dark mb-4">Mais do que seguros,<br/><span class="text-gradient-gold">tranquilidade</span> em todas as áreas</h2>
          <div class="w-16 h-1 bg-toth-gold mx-auto rounded-full mb-8"></div>
          
          <div class="inline-flex rounded-xl p-1 bg-gray-200 border border-gray-100 shadow-inner mb-6 mx-auto">
            <button id="btn-voce" onclick="switchTab('voce')" class="tab-btn active-tab-btn relative px-6 py-2.5 text-sm font-bold text-gray-900 bg-white rounded-lg shadow-sm transition-all focus:outline-none">Para Você e Família</button>
            <button id="btn-empresa" onclick="switchTab('empresa')" class="tab-btn px-6 py-2.5 text-sm font-medium text-gray-600 rounded-lg hover:text-gray-900 transition-all focus:outline-none">Para Empresas</button>
          </div>
        </div>

        <!-- Tab: VOCÊ -->
        <div id="tab-voce" class="tab-content block animate-fade-in">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7">
            <a href="seguro-auto.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-car"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Seguro Auto</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Proteção completa para seu veículo contra colisões, furtos e danos a terceiros.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="seguro-residencial.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-home"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Seguro Residencial</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Garanta a segurança da sua casa contra incêndios, vendavais e danos elétricos.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="seguro-de-vida.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-heart"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Seguro de Vida</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Apoio e planejamento financeiro para manter o padrão de vida de quem você mais ama.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="plano-de-saude.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-user-doctor"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Planos de Saúde</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Ampla cobertura e parceiros reconhecidos para a saúde e bem-estar em todas as idades.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="seguro-equipamentos.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-mobile-screen"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Equipamentos Portáteis</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Proteção contra roubo e quebra acidental de celulares, tablets, câmeras e notebooks.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="consorcios.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-house-circle-check"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Consórcios</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Planejamento financeiro sem juros abusivos para comprar seu imóvel ou trocar de veículo.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
          </div>
        </div>

        <!-- Tab: EMPRESA -->
        <div id="tab-empresa" class="tab-content hidden animate-fade-in">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7 justify-center">
            <a href="seguro-empresarial.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-city"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Seguro Empresarial</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Mantenha a operação em dia cobrindo a estrutura física (incêndio) e os bens da empresa.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="responsabilidade-civil.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-scale-balanced"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Resp. Civil (RC)</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Defesa e indenizações contra danos a terceiros ocorridos durante o fornecimento dos seus serviços.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="seguro-de-pessoas.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-people-group"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Vida em Grupo</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Segurança corporativa para sócios e colaboradores, gerando valor no pacote de benefícios (RH).</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
            <a href="seguro-de-danos-patrimoniais.php/index.html" class="service-card group block bg-white rounded-2xl p-7 shadow-[0_4px_20px_rgb(0,0,0,0.04)] border border-gray-100 hover:border-toth-goldLight transition-all">
              <div class="icon-wrap w-14 h-14 rounded-xl bg-toth-light flex items-center justify-center text-2xl text-toth-gold mb-5 shadow-sm group-hover:scale-110 transition-transform"><i class="fa fa-warehouse"></i></div>
              <h3 class="text-lg font-bold text-gray-900 mb-2">Danos Patrimoniais</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-4">Garantia para maquinários pesados, construção civil e indústrias mediante intempéries e lucros cessantes.</p>
              <span class="text-toth-gold text-xs font-bold uppercase tracking-wider group-hover:underline">Saiba Mais <i class="fa fa-arrow-right ml-1"></i></span>
            </a>
          </div>
        </div>

      </div>
    </section>

"""

# Novo bloco Testemunhos
new_testimonials = """    <!-- ===== O QUE DIZEM NOSSOS CLIENTES (PROVA SOCIAL) ===== -->
    <section class="py-20 bg-toth-light border-y border-gray-100 relative overflow-hidden">
      <div class="absolute top-0 right-0 w-64 h-64 bg-toth-gold rounded-full blur-[100px] opacity-10"></div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="inline-block py-1 px-3 rounded-full bg-toth-gold/20 border border-toth-gold/30 text-toth-gold text-xs font-bold tracking-widest uppercase mb-3">Reconhecimento</span>
          <h2 class="text-3xl md:text-4xl font-extrabold text-toth-dark mb-4">
            A escolha de quem busca <span class="text-gradient-gold">Segurança</span>
          </h2>
          <div class="w-16 h-1 bg-toth-gold mx-auto rounded-full"></div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Card de Depoimento 1 -->
          <div class="bg-white rounded-2xl p-8 shadow-[0_5px_20px_rgb(0,0,0,0.03)] border border-gray-100 relative">
            <i class="fa fa-quote-left text-4xl text-gray-100 absolute top-6 right-6"></i>
            <div class="flex text-amber-400 text-sm mb-4">
              <i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i>
            </div>
            <p class="text-gray-600 italic leading-relaxed mb-6">"Atendimento super rápido e claro quando precisei acionar o meu Seguro Auto. Foi a melhor transição de corretora que fiz. Recomendo!"</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center font-bold overflow-hidden"><img src="https://i.pravatar.cc/100?img=11" alt="Roberto Silas" class="w-full h-full object-cover"></div>
              <div>
                <h4 class="font-bold text-gray-900 text-sm">Roberto Silas</h4>
                <p class="text-xs text-gray-500">Curitiba, PR</p>
              </div>
            </div>
          </div>

          <!-- Card de Depoimento 2 -->
          <div class="bg-white rounded-2xl p-8 shadow-[0_5px_20px_rgb(0,0,0,0.03)] border border-gray-100 relative">
            <i class="fa fa-quote-left text-4xl text-gray-100 absolute top-6 right-6"></i>
            <div class="flex text-amber-400 text-sm mb-4">
              <i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i>
            </div>
            <p class="text-gray-600 italic leading-relaxed mb-6">"Eles ajudaram na escolha do Plano de Saúde perfeito para minha família com muita transparência. O suporte fez a diferença."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center font-bold overflow-hidden"><img src="https://i.pravatar.cc/100?img=5" alt="Mariana Costa" class="w-full h-full object-cover"></div>
              <div>
                <h4 class="font-bold text-gray-900 text-sm">Mariana Costa</h4>
                <p class="text-xs text-gray-500">São Paulo, SP</p>
              </div>
            </div>
          </div>

          <!-- Card de Depoimento 3 -->
          <div class="bg-white rounded-2xl p-8 shadow-[0_5px_20px_rgb(0,0,0,0.03)] border border-gray-100 relative">
            <i class="fa fa-quote-left text-4xl text-gray-100 absolute top-6 right-6"></i>
            <div class="flex text-amber-400 text-sm mb-4">
              <i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i><i class="fa fa-solid fa-star"></i>
            </div>
            <p class="text-gray-600 italic leading-relaxed mb-6">"Fechamos o Seguro Empresarial do nosso galpão em tempo recorde e excelente preço. A consultoria ajudou nossa decisão final."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center font-bold overflow-hidden"><img src="https://i.pravatar.cc/100?img=53" alt="Carlos Mendes" class="w-full h-full object-cover"></div>
              <div>
                <h4 class="font-bold text-gray-900 text-sm">Carlos Mendes</h4>
                <p class="text-xs text-gray-500">Rio de Janeiro, RJ</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== DIFERENCIAIS ===== -->"""

# Script Tabs
new_script = """    <!-- Script UI -->
    <style>
      .animate-fade-in { animation: fadeIn 0.4s ease-in-out; }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
      .active-tab-btn { background-color: white; color: #111; font-weight: bold; border: 1px solid #d1d5db; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    </style>
    <script>
      function switchTab(target) {
        document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
        document.getElementById('tab-' + target).classList.remove('hidden');
        document.querySelectorAll('.tab-btn').forEach(btn => {
          btn.classList.remove('active-tab-btn', 'bg-white', 'text-gray-900', 'shadow-sm', 'font-bold');
          btn.classList.add('text-gray-600', 'font-medium');
          btn.style.border = 'none';
        });
        const activeBtn = document.getElementById('btn-' + target);
        activeBtn.classList.add('active-tab-btn', 'bg-white', 'text-gray-900', 'shadow-sm', 'font-bold');
        activeBtn.classList.remove('text-gray-600', 'font-medium');
      }
    </script>
</body>"""

# Perform Replacements
content = re.sub(
    r'<!-- ===== SERVICES GRID ===== -->.*?(?=<!-- ===== SIMULAÇÃO ===== -->)',
    new_services + "\\n    ",
    content,
    flags=re.DOTALL
)

content = content.replace("<!-- ===== DIFERENCIAIS ===== -->", new_testimonials)
content = content.replace("</body>", new_script)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement successful!")
