import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="Batman.py", icon="assets/bman.png"
)]


cx_Freeze.setup(
    name="Dark Knight do Pedrinho",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)


# python setup.py build (aqui ele vair gerar uma pasta com os arquivos dentro)
# python setup.py bdist_msi (aqui ele gera um instalador de windows)
