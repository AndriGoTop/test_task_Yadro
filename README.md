POST /api/graph/ -- Записывает новый асинхронный граф. Запрашивает (query) nodes: list[str] и adjacency_list: dict[str, list[str]] <br/>
GET /api/graph/{graph_id}/ -- Находит граф по id. Запрашивает graph_id: int <br/>
GET /api/graph/{graph_id}/adjacency_list -- Выводит список смежности по id. Запрашивает graph_id: int <br/>
