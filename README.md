# pano-to-mesh-server
On-premise of pano-to-mesh

# DB Schema 
```mermaid
erDiagram
    Room {
        string id PK
        object decorations
        string user_id FK
    }
    PanoInfo{
        string id PK
        string user_id FK
    }
    Texture {
        string id PK
        string image_url
        string panoInfo_id FK
    }
    Layout {
        string id PK
        string coords
        string panoInfo_id FK
    }

    Room-PanoInfo {
        string room_id PK, FK
        string panoInfo_id PK, FK
    }

    User {
        string id PK
        string name
    }
    
    PanoInfo ||--|{ Room-PanoInfo : used
    Room ||--|{ Room-PanoInfo : contains
    PanoInfo ||--o{ Texture: has
    PanoInfo ||--|| Layout: has
    User ||--o{ Room: has
    User ||--o{ PanoInfo: has
```
