import re

filepath = r"c:\projetos\landing_page\site-toth-clonado\site\pages\index.php\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir o href problemático usando o nome do h3 correspondente
replacements = {
    "Seguro Auto": "seguro-auto.php",
    "Seguro Residencial": "seguro-residencial.php",
    "Seguro de Vida": "seguro-de-vida.php",
    "Planos de Saúde": "plano-de-saude.php",
    "Equipamentos Portáteis": "seguro-equipamentos.php",
    "Consórcios": "consorcios.php",
    "Seguro Empresarial": "seguro-empresarial.php",
    "Resp. Civil ": "responsabilidade-civil.php",
    "Vida em Grupo": "seguro-de-pessoas.php",
    "Danos Patrimoniais": "seguro-de-danos-patrimoniais.php"
}

# Procurar cada bloco <a href="../"...> ... <h3>NOME</h3>
for h3_text, folder in replacements.items():
    # Regex para achar a tag <a> antes do h3
    pattern = r'(<a href="\.\./"[^>]*>[\s\S]*?<h3[^>]*>)' + re.escape(h3_text)
    # Substituir no padrão:
    def repl(m):
        return m.group(1).replace('href="../"', f'href="../{folder}/index.html"') + h3_text
    
    content = re.sub(pattern, repl, content, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Links corrigidos!")
