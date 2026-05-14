from __future__ import annotations

from pytm import TM, Actor, Boundary, Classification, Data, Datastore, Dataflow, Process


def build_model() -> TM:
        """
        PyTM model aligned to the current TypeSpec (5 components):
            - RAGClient (Internet)
            - GatewayService (DMZ)
            - IngestionWorker (Trusted)
            - InferenceEngine (Trusted)
            - VectorDatastore (HighSide)

        Flow types mirror @dataFlow decorators: Control, Ingestion, Retrieval, ContextInjection, Inference.
        """
        tm = TM("Gemini Managed RAG")
        tm.description = "Managed RAG architecture: client -> gateway -> ingestion -> vector store -> inference engine"

        # Trust zones
        internet = Boundary("Internet")
        dmz = Boundary("DMZ")
        trusted = Boundary("Trusted")
        highside = Boundary("HighSide")

        # Components (match TypeSpec namespaces)
        client = Actor("RAGClient")
        client.inBoundary = internet

        gateway = Process("GatewayService")
        gateway.inBoundary = dmz

        ingestion = Process("IngestionWorker")
        ingestion.inBoundary = trusted

        inference = Process("InferenceEngine")
        inference.inBoundary = trusted

        vector_store = Datastore("VectorDatastore")
        vector_store.inBoundary = highside
        vector_store.isEncrypted = True

        # Data objects (aligned to classification levels)
        user_query = Data("User Query")
        user_query.classification = Classification.SENSITIVE  # Internal

        uploaded_doc = Data("Uploaded Document")
        uploaded_doc.classification = Classification.SENSITIVE  # Confidential

        embeddings = Data("Embeddings")
        embeddings.classification = Classification.RESTRICTED

        context_chunks = Data("Retrieved Context")
        context_chunks.classification = Classification.RESTRICTED

        model_response = Data("Model Response")
        model_response.classification = Classification.PUBLIC

        # Flows (align to TypeSpec semantic flows)

        # 1) routeRequest: Client -> Gateway (Control)
        q1 = Dataflow(client, gateway, "routeRequest")
        q1.protocol = "HTTPS"
        q1.data = user_query
        q1.flowType = "Control"

        # 2) processUpload: Client -> Gateway -> Ingestion (Ingestion)
        u1 = Dataflow(client, gateway, "upload: submit document")
        u1.protocol = "HTTPS"
        u1.data = uploaded_doc
        u1.flowType = "Ingestion"

        u2 = Dataflow(gateway, ingestion, "processUpload")
        u2.protocol = "HTTPS"
        u2.data = uploaded_doc
        u2.flowType = "Ingestion"

        # 3) generateEmbeddings: Ingestion -> Vector store (Control)
        u3 = Dataflow(ingestion, vector_store, "generateEmbeddings")
        u3.protocol = "gRPC"
        u3.data = embeddings
        u3.flowType = "Control"

        # 4) query to inference: Gateway -> InferenceEngine (Control)
        g1 = Dataflow(gateway, inference, "query")
        g1.protocol = "HTTPS"
        g1.data = user_query
        g1.flowType = "Control"

        # 5) fetchEmbeddings: InferenceEngine -> Vector store (Retrieval)
        r1 = Dataflow(inference, vector_store, "fetchEmbeddings")
        r1.protocol = "gRPC"
        r1.data = embeddings
        r1.flowType = "Retrieval"

        # 6) returnChunks: Vector store -> InferenceEngine (ContextInjection)
        r2 = Dataflow(vector_store, inference, "returnChunks")
        r2.protocol = "gRPC"
        r2.data = context_chunks
        r2.flowType = "ContextInjection"

        # 7) generateResponse: InferenceEngine -> Gateway (Inference)
        i1 = Dataflow(inference, gateway, "generateResponse")
        i1.protocol = "HTTPS"
        i1.data = model_response
        i1.flowType = "Inference"

        # 8) deliver response: Gateway -> Client (Inference)
        resp = Dataflow(gateway, client, "deliverResponse")
        resp.protocol = "HTTPS"
        resp.data = model_response
        resp.flowType = "Inference"

        return tm
