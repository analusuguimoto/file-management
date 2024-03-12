def exists_word(word, instance):
    words_info = []
    for data in range(len(instance)):
        ocurrencies = []
        info = instance.search(data)

        for index, line in enumerate(info["linhas_do_arquivo"], start=1):
            if word in line.lower():
                ocurrencies.append({"linha": index})

        if ocurrencies:
            result = {
                "palavra": word,
                "arquivo": info["nome_do_arquivo"],
                "ocorrencias": ocurrencies,
            }
            words_info.append(result)

    return words_info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
