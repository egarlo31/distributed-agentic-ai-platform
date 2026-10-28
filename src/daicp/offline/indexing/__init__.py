"""Approved document ingestion, chunking and knowledge index construction."""
from .pipeline import KnowledgeIndexer, ApprovedDocument

__all__ = ["KnowledgeIndexer", "ApprovedDocument"]
