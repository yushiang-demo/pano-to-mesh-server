# pano-to-mesh-server
On-premise of pano-to-mesh

# DbSchema 
```mermaid
erDiagram

    Room {
        string id PK
        string[] panorama_id FK
        string layout_id FK
        string decorations_id FK
    }
    Room }|--|{ Panorama : has
    Panorama {
        string id PK
        string image_url
    }
    Panorama }|--|| Layout : has
    Layout {
        string id PK
        object coords
    }
    Room ||--|| Decorations : has
    Decorations {
        string id PK
        object items
    }
```
