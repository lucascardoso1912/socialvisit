from ia import gerar_descricao_tecnica
import pandas as pd
from docx import Document
from pathlib import Path
from database import criar_banco, inserir_visita, visita_existe

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "visitas.csv"
TEMPLATE_FILE = BASE_DIR / "templates" / "relatorio_template.txt"
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

criar_banco()
df = pd.read_csv(DATA_FILE, encoding="utf-8")
df["data_visita"] = pd.to_datetime(df["data_visita"], format="%d-%m-%Y")

with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
    template = file.read()

inseridas = 0

for _, row in df.iterrows():

    descricao_tecnica = gerar_descricao_tecnica(row["observacao"])

    texto = template.format(
        familia=row["familia"],
        data_visita=row["data_visita"].strftime("%d-%m-%Y"),
        tecnico=row["tecnico"],
        risco=row["risco"],
        observacao=descricao_tecnica,
        encaminhamento=row["encaminhamento"]
    )

    doc = Document()
    doc.add_paragraph(texto)

    nome_arquivo = f"{row['familia']}_{row['data_visita'].strftime('%d-%m-%Y')}.docx"
    doc.save(REPORTS_DIR / nome_arquivo)

    data_iso = row["data_visita"].strftime("%Y-%m-%d")

    if not visita_existe(row["familia"], data_iso):
        inserir_visita(
            familia=row["familia"],
            data_visita=data_iso,
            tecnico=row["tecnico"],
            anotacoes_brutas=row["observacao"],
            descricao_tecnica=descricao_tecnica,
            risco=row["risco"],
            encaminhamentos=row["encaminhamento"]
        )
        inseridas += 1
    else:
        print(f"Visita já existe no banco: {row['familia']} - {data_iso}")

print(f"Relatórios gerados com sucesso. {inseridas} novas visitas salvas no banco.")
