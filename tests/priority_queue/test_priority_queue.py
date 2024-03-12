from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 2})
    queue.enqueue({"qtd_linhas": 8})
    queue.enqueue({"qtd_linhas": 6})

    assert len(queue) == 4
    assert len(queue.high_priority) == 2
    assert len(queue.regular_priority) == 2

    queue.dequeue()
    assert len(queue) == 3

    project_search = queue.search(1)
    assert project_search["qtd_linhas"] == 8

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(9)
