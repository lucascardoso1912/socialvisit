import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "socialvisit.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        familia TEXT NOT NULL,
        data_visita DATE NOT NULL,
        tecnico TEXT NOT NULL,
        anotacoes_brutas TEXT NOT NULL,
        descricao_tecnica TEXT NOT NULL,
        risco TEXT CHECK (risco IN ('Baixo', 'Médio', 'Alto')) NOT NULL,
        encaminhamentos TEXT,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

def inserir_visita(
    familia,
    data_visita,
    tecnico,
    anotacoes_brutas,
    descricao_tecnica,
    risco,
    encaminhamentos
):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO visitas (
        familia,
        data_visita,
        tecnico,
        anotacoes_brutas,
        descricao_tecnica,
        risco,
        encaminhamentos
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        familia,
        data_visita,
        tecnico,
        anotacoes_brutas,
        descricao_tecnica,
        risco,
        encaminhamentos
    ))

    conn.commit()
    conn.close()

def visita_existe(familia, data_visita):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM visitas
        WHERE familia = ? AND data_visita = ?
        LIMIT 1
    """, (familia, data_visita))

    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def buscar_visitas_familia(familia):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            data_visita,
            tecnico,
            descricao_tecnica,
            risco,
            encaminhamentos
        FROM visitas
        WHERE familia = ?
        ORDER BY data_visita
    """, (familia,))

    resultados = cursor.fetchall()
    conn.close()
    return resultados
