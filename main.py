from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Graphs(BaseModel):
    nodes: list[str]
    adjacency_list: dict[str, list[str]]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def search_cycle(data: Graphs, node, path_graph: list = []):
        path_graph.append(node)
        for targs in data.adjacency_list[node]:
            if not (targs in path_graph):
                return search_cycle(data, targs, path_graph)
            else:
                print(path_graph)
                return True
        return False

@app.post('/api/graph/')
async def create_graph(graph: Annotated[Graphs, Depends()], db: db_dependency):
    res = False
    nodes = [graph.nodes[i] for i in range(len(graph.nodes))]
    for node in nodes:
        res |= search_cycle(graph, node, [])
    if res:
        return {'Error': 'Цикличный граф'}
    db_graphs = models.Graphs(nodes=str(graph.nodes), adjency_list=str(graph.adjacency_list))
    db.add(db_graphs)
    db.commit()
    print(str(graph.nodes))
    return {'Data': str(graph.nodes)}

test = {
    "nodes":["a", "b", "c", "d"],
    "adjacency_list":{"a": ["c"],
                      "c":["d"],
                      "d":[],
                      "b": ["c"]}
}

@app.get('/api/graph/{graph_id}/')
async def get_graph(graph_id, db: db_dependency):
    result = db.query(models.Graphs).filter(models.Graphs.id == graph_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Graph entity not found')
    return result

@app.get('/api/graph/{graph_id}/adjacency_list')
async def get_graph(graph_id, db: db_dependency):
    result = db.query(models.Graphs).filter(models.Graphs.id == graph_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Graph entity not found')
    return result.adjency_list
