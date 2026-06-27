### 🗺️ Diagrama Visual de la Arquitectura de Datos de Yape

```mermaid
graph TD
    %% Estilos Generales
    classDef trans fill:#4A90E2,stroke:#333,stroke-width:2px,color:#fff;
    classDef nosql fill:#F5A623,stroke:#333,stroke-width:2px,color:#fff;
    classDef analitica fill:#7ED321,stroke:#333,stroke-width:2px,color:#fff;
    classDef spark fill:#E67E22,stroke:#333,stroke-width:2px,color:#fff;

    %% Definición de Nodos de Entrada
    USUARIO[📱 Cliente / Comercio Yape] -->|Peticiones masivas| API[⚡ API Gateway / Balanceador]

    %% Capa Transaccional y Tiempo Real
    subgraph Capa Transaccional & Estado
        API -->|Autenticación rápida| REDIS[(🔑 Redis: In-Memory)]
        API -->|Gestión Transaccional| POSTGRES[(💰 PostgreSQL / CockroachDB)]
        API -->|Estructuras dinámicas| MONGO[(🏪 MongoDB Local / Atlas)]
    end

    %% Capa de Seguridad y Relaciones
    subgraph Detección de Fraude en Tiempo Real
        POSTGRES -->|Ingesta continua de eventos| NEO4J(((🕵️ Neo4j: Red de Fraude)))
        NEO4J -->|Alerta inmediata de ciclos| API
    end

    %% Capa de Big Data y Analítica
    subgraph Capa de Almacenamiento Masivo y BI
        POSTGRES -.->|ETL / Replicación CDC| DATABRICKS[🔥 Databricks: Apache Spark + Delta Lake]
        MONGO -.->|Carga de Catálogos| DATABRICKS
        DATABRICKS -->|Procesamiento de 18 TB/año| CLICKHOUSE[(📈 ClickHouse / Analítica)]
        CLICKHOUSE -->|Consumo diario| DASHBOARD[📊 Dashboard Ejecutivo BI]
    end

    %% Asignación de Estilos
    class POSTGRES,REDIS trans;
    class MONGO,NEO4J nosql;
    class CLICKHOUSE,DASHBOARD analitica;
    class DATABRICKS spark;