from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for name in instance.queue:
        if name["nome_do_arquivo"] == path_file:
            return name

    lines_info = txt_importer(path_file)
    if lines_info is not None:
        dicti = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines_info),
            "linhas_do_arquivo": lines_info,
        }

    instance.enqueue(dicti)
    sys.stdout.write(str(dicti))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    file_rmv = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file_rmv['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        info = instance.search(position)
        sys.stdout.write(str(info))
    except IndexError:
        sys.stderr.write("Posição inválida")
