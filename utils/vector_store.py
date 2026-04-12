"""向量库操作封装 — 支持 Chroma 和 FAISS，提供统一的 add/query 接口。"""

from pathlib import Path


class SimpleVectorStore:
    """基于 ChromaDB 的简单向量库封装，适用于 RAG 学习场景。

    Usage:
        store = SimpleVectorStore("my_collection")
        store.add_texts(["doc1", "doc2"], ids=["1", "2"])
        results = store.query("search text", n_results=3)
    """

    def __init__(self, collection_name: str, persist_dir: str | None = None):
        import chromadb

        if persist_dir:
            self.client = chromadb.PersistentClient(path=persist_dir)
        else:
            self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(name=collection_name)
        self.collection_name = collection_name

    def add_texts(
        self,
        documents: list[str],
        ids: list[str] | None = None,
        metadatas: list[dict] | None = None,
    ) -> None:
        """添加文本到向量库。"""
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(documents=documents, ids=ids, metadatas=metadatas)

    def query(self, query_text: str, n_results: int = 5) -> dict:
        """查询最相似的文档。"""
        return self.collection.query(query_texts=[query_text], n_results=n_results)

    @property
    def count(self) -> int:
        return self.collection.count()


def build_faiss_index(embeddings_list: list[list[float]], dimension: int | None = None):
    """快速构建 FAISS 向量索引 — 用于推荐系统和大规模检索场景。

    Args:
        embeddings_list: 向量列表 [[0.1, 0.2, ...], ...]
        dimension: 向量维度，None 则自动推断

    Returns:
        faiss.IndexFlatL2 索引对象
    """
    import numpy as np
    import faiss

    embeddings = np.array(embeddings_list, dtype="float32")
    dim = dimension or embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index
