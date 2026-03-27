import os
import re

directory = r"c:\projetos\landing_page\site-toth-clonado\site\pages"

mappings = {
    'seguro-auto.php': 'seguro-auto',
    'seguro-residencial.php': 'seguro-residencial',
    'seguro-equipamentos.php': 'seguro-equipamentos',
    'seguro-empresarial.php': 'seguro-empresarial',
    'seguro-de-pessoas.php': 'seguro-de-pessoas',
    'seguro-de-vida.php': 'seguro-de-vida',
    'seguro-de-danos-patrimoniais.php': 'seguro-de-danos-patrimoniais',
    'responsabilidade-civil.php': 'responsabilidade-civil',
    'consorcios.php': 'consorcios',
    'plano-de-saude.php': 'plano-de-saude',
    'planos-de-saude.php': 'plano-de-saude'
}

pattern = re.compile(r'<div class="bg-gray-50 border border-gray-100 rounded-2xl p-6">\s*<h3 class="font-bold text-gray-900 text-lg mb-4">\s*Outros Serviços\s*<\/h3>\s*<nav class="sidebar-nav space-y-1">.*?<\/nav>\s*<\/div>', re.DOTALL)

for folder, active_id in mappings.items():
    filepath = os.path.join(directory, folder, 'index.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            replacement = f'<toth-sidebar-services active="{active_id}" base="../../"></toth-sidebar-services>'
            new_content = pattern.sub(replacement, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Pattern not found in {filepath}")
    else:
        print(f"File not found: {filepath}")
