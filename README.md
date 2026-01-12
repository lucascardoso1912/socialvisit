SocialVisit – Sistema de Avaliação, Registro e Histórico de Risco

## 📖 Visão Geral

Este projeto é um sistema em **Python** desenvolvido para automatizar a elaboração de relatórios técnicos, organizar registros de avaliações periódicas, classificar níveis de risco e manter histórico estruturado para auditoria e tomada de decisão.

**O projeto nasceu a partir de um problema real de operação**, onde havia grande volume de registros manuais, dificuldade de consulta histórica e alto tempo gasto na elaboração de relatórios. A solução proposta automatiza esses processos, mantendo rastreabilidade, organização e padronização.

Embora aplicado inicialmente a um contexto social, o modelo é genérico e aplicável a cenários de Governança, Risco e Conformidade (GRC), como Third-Party Cyber Risk Management (TPCRM), onde há necessidade de:

- avaliação periódica de entidades
- análise de evidências
- classificação de risco
- acompanhamento de pendências
- geração de relatórios técnicos e históricos

---

## Objetivos do Projeto

- Automatizar a geração de relatórios técnicos diários
- Estruturar dados de avaliações em banco de dados
- Manter histórico confiável por entidade avaliada
- Facilitar respostas rápidas em situações imprevistas
- Apoiar processos de análise de risco e auditoria

## Funcionalidades Principais
 
### ✔️ Geração de Relatórios Técnicos

- Entrada de anotações brutas (texto informal ou palavras-chave)
- Geração automática de relatórios técnico padronizado (DOCX)
- Datas formatadas no padrão brasileiro

### ✔️ Avaliação de Risco

- Classificação manual de risco (Baixo, Médio, Alto)
- Registro do risco por avaliação
- Visualização da evolução de risco ao longo do tempo

### ✔️ Banco de Dados Histórico

- Armazenamento em SQLite
- Processamento e transformação de dados estruturados utilizando **pandas**
- Histórico completo por entidade avaliada
- Proteção contra duplicidade de registros
- Rastreamento temporal (timestamp)


### ✔️ Relatório Histórico por Entidade

- Consolidação de todas as avaliações
- Linha do tempo cronológica
- Evolução do risco
- Descrições técnicas e encaminhamentos

---

## Arquitetura do Projeto
```
socialvisit/
├─ src/
│  ├─ main.py                # Geração de relatórios diários
│  ├─ database.py            # Banco de dados e consultas
│  ├─ historico_familia.py   # Relatório histórico por entidade
│  ├─ ia.py                  # Apoio à redação técnica
│  └─ ia_prompt.py           # Regras e prompt da IA (desacoplado)
│
├─ templates/
│  └─ relatorio_template.txt
│
├─ data/
│  └─ README.md              # Dados reais não versionados
│
├─ reports/
│  └─ README.md              # Relatórios gerados localmente
│
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## Segurança e Boas Práticas

- Dados sensíveis (CSV, banco SQLite e relatórios) não são versionados
- Uso de queries parametrizadas para evitar SQL Injection
- Separação entre código, dados e relatórios
- Arquitetura preparada para integração segura com IA
- Histórico com timestamp para auditoria

## Como Executar o Projeto
1 Instalar dependências
pip install -r requirements.txt

2️ Gerar relatórios diários
python src/main.py

3️ Gerar relatório histórico por entidade
python src/historico_familia.py

## Aplicação em TPCRM e GRC

O modelo deste sistema é diretamente aplicável a processos de Third-Party Cyber Risk Management, pois trabalha com:

- registro de evidências
- avaliações periódicas
- classificação de risco
- acompanhamento de pendências
- documentação técnica e auditoria

A adaptação para TPCRM exige apenas mudança de contexto de domínio, mantendo a mesma arquitetura e lógica.

## Próximos Passos (Updates)

- Integração com IA via API para redação técnica avançada
- Resumo técnico automático de 1 página
- Interface simplificada para uso operacional
- Dashboards de risco

---

## 👤 Autor

**Lucas Cardoso Rocha**            
**Estudante de Segurança Cibernética**

Este projeto foi desenvolvido para **automatizar uma operação real**, visando reduzir tempo operacional, melhorar a organização das informações e facilitar a consulta histórica e a tomada de decisão.
Posteriormente, o sistema foi **estruturado, documentado e adaptado para fins de portfólio**, preservando a lógica e os desafios reais do problema original, sem expor dados sensíveis ou informações institucionais.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
