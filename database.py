import sqlite3
import pandas as pd

# Inisialisasi koneksi (gunakan file SQLite)
conn = sqlite3.connect("bee_alaska.db", check_same_thread=False)
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS neraca_saldo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    akun TEXT,
    debit REAL,
    kredit REAL
)
""")
conn.commit()

# Fungsi untuk menyimpan data saldo awal
def simpan_saldo(akun, debit, kredit):
    cursor.execute("""
        INSERT INTO neraca_saldo (akun, debit, kredit)
        VALUES (?, ?, ?)
    """, (akun, debit, kredit))
    conn.commit()

# Fungsi untuk mengambil data neraca saldo
def ambil_saldo():
    return pd.read_sql("""
        SELECT akun AS 'Nama Akun', debit AS 'Debit', kredit AS 'Kredit'
        FROM neraca_saldo
    """, conn)
    
# Fungsi untuk hapus data jika diperlukan
def hapus_semua_saldo():
    cursor.execute("DELETE FROM neraca_saldo")
    conn.commit()

# Tabel Jurnal Umum
cursor.execute("""
CREATE TABLE IF NOT EXISTS jurnal_umum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    akun TEXT,
    keterangan TEXT,
    debit REAL,
    kredit REAL
)
""")
conn.commit()

# Fungsi untuk menyimpan entri jurnal
def simpan_jurnal(tanggal, akun, keterangan, debit, kredit):
    cursor.execute("""
        INSERT INTO jurnal_umum (tanggal, akun, keterangan, debit, kredit)
        VALUES (?, ?, ?, ?, ?)
    """, (tanggal, akun, keterangan, debit, kredit))
    conn.commit()

# Fungsi untuk mengambil jurnal
def ambil_jurnal():
    return pd.read_sql("""
        SELECT tanggal AS 'Tanggal', akun AS 'Nama Akun', 
               keterangan AS 'Keterangan', debit AS 'Debit', kredit AS 'Kredit' 
        FROM jurnal_umum
    """, conn)