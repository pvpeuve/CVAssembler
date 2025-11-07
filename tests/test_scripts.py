from pathlib import Path
import subprocess

def test_unir_secciones():
    assert subprocess.run(["python3", "scripts/unir_secciones.py"]).returncode == 0

def test_exportar_md_a_pdf():
    # Solo prueba que el script no falla (sin Pandoc completo)
    subprocess.run(["python3", "scripts/exportar_md_a_pdf.py"], check=False)
